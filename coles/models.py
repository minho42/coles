from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from project.models import TimeStampedModel


class Coles(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.0)
    note = models.TextField(max_length=256, null=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{'✅' if self.is_available else '❎'}: {self.card_number[:4]}...{self.card_number[-4:]}: {self.balance}"

    class Meta:
        unique_together = [["user", "card_number"]]
