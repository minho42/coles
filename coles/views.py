from typing import final
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.utils.timezone import now

from .scraper import get_balance
from .models import Coles


@login_required
def sync(request):

    cards = Coles.objects.filter(user=request.user.id)
    for card in cards:
        try:
            c = get_object_or_404(Coles, id=card.id)
            c.balance = 0
            c.is_last_sync_success = False

            balance = get_balance(card.card_number, card.pin)
            print(balance)

            c.balance = float(balance)
            c.is_last_sync_success = True
            c.last_sync_time = now()
            c.save()
            messages.success(request, f"Synced: {card.card_number}")
        except:
            messages.error(request, f"Something went wrong: {card.card_number}")
        finally:
            c.save()
    return HttpResponseRedirect(reverse("coles:list"))


class ColesListView(LoginRequiredMixin, ListView):
    model = Coles

    def get_queryset(self):
        return Coles.objects.filter(user=self.request.user).order_by(
            "last_sync_time", "-is_last_sync_success", "balance", "-created"
        )


class ColesCreateView(LoginRequiredMixin, CreateView):
    model = Coles
    fields = ["card_number", "pin"]
    template_name = "coles/coles_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user

        try:
            success_url = super().form_valid(form)
            form.instance.save()
            messages.success(self.request, f"Added: {form.cleaned_data['card_number']}")
            return success_url

        except IntegrityError:
            messages.error(self.request, f"You've already added [{form.instance.card_number}]")
            return HttpResponseRedirect(reverse("coles:add"))


class ColesDetailView(LoginRequiredMixin, DetailView):
    model = Coles


class ColesDeleteView(LoginRequiredMixin, DeleteView):
    model = Coles
    success_url = reverse_lazy("coles:list")
