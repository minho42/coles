from typing import final
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.utils.timezone import now
from core.utils import which_settings
from .barcode_generator import generate_barcode
from .scraper import get_balance
from .models import Coles


@login_required
def sync(request):

    cards = Coles.objects.filter(user=request.user.id)
    for card in cards:
        try:
            balance = get_balance(card.short_card_number, card.pin)
            print(balance)

            card.balance = float(balance)
            card.is_last_sync_success = True
            card.last_sync_time = now()
            card.save()
            messages.success(request, f"Synced: {card.short_card_number}: ${card.balance}")
        except:
            card.balance = 0
            card.is_last_sync_success = False
            card.save()
            messages.error(request, f"Something went wrong: {card.short_card_number}")
    return HttpResponseRedirect(reverse("coles:list"))


class ColesListView(LoginRequiredMixin, ListView):
    model = Coles

    def get_queryset(self):
        return Coles.objects.filter(user=self.request.user).order_by(
            "last_sync_time", "-is_last_sync_success", "balance", "-created"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_production"] = which_settings() == "production"
        return context


class ColesCreateView(LoginRequiredMixin, CreateView):
    model = Coles
    fields = ["card_number", "pin", "balance"]
    template_name = "coles/coles_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user

        try:
            success_url = super().form_valid(form)
            new_card_number = form.cleaned_data["card_number"]
            if generate_barcode(new_card_number, form.instance.barcode_fullpath_without_extension):
                form.instance.barcode_filename = form.instance.barcode_filename_with_extension

            form.instance.save()
            messages.success(self.request, f"Added: {new_card_number}")
            return success_url

        except IntegrityError:
            messages.error(self.request, f"You've already added [{form.instance.card_number}]")
            return HttpResponseRedirect(reverse("coles:add"))


class ColesDetailView(LoginRequiredMixin, DetailView):
    model = Coles


class ColesDeleteView(LoginRequiredMixin, DeleteView):
    model = Coles
    success_url = reverse_lazy("coles:list")
