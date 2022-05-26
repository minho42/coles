from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .api import get_balance
from .models import Coles


@login_required
def sync(request):

    cards = Coles.objects.filter(user=request.user.id)
    for card in cards:
        balance = get_balance(card.card_number, card.pin)
        print(balance)
        c = get_object_or_404(Coles, id=card.id)
        c.balance = float(balance)
        c.save()
    return HttpResponseRedirect(reverse("coles:list"))


class ColesListView(LoginRequiredMixin, ListView):
    model = Coles
    template_name = "coles/coles_list.html"
    context_object_name = "coles_cards"

    def get_queryset(self):
        return Coles.objects.filter(user=self.request.user).order_by("-created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coles_cards_count"] = Coles.objects.filter(user=self.request.user).count()
        context["coles_cards_count_available"] = (
            Coles.objects.filter(user=self.request.user).filter(is_available=True).count()
        )
        return context


class ColesCreateView(LoginRequiredMixin, CreateView):
    model = Coles
    template_name = "coles/coles_create.html"


class ColesDetailView(LoginRequiredMixin, DetailView):
    model = Coles
    template_name = "coles/coles_detail.html"

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(user=self.request.user)
    #     return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ColesUpdateView(LoginRequiredMixin, UpdateView):
    model = Coles
    fields = ["card_number", "pin", "note"]
    template_name = "coles/coles_update.html"


class ColesDeleteView(LoginRequiredMixin, DeleteView):
    model = Coles
    success_url = reverse_lazy("coles:list")

    # GET request display confirmation template, while POST deletes instance
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
