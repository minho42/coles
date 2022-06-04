from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from project.models import TimeStampedModel


class Coles(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card_number = models.CharField(max_length=30)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.0)
    is_last_sync_success = models.BooleanField(default=False)
    last_sync_time = models.DateTimeField(auto_now=False, null=True)
    barcode_filename = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.card_number[:4]}...{self.card_number[-4:]}: {self.balance}"

    class Meta:
        unique_together = [["user", "card_number"]]

    def get_absolute_url(self):
        return reverse("coles:list")

    @property
    def short_card_number(self):
        return self.card_number[-17:]

    @property
    def barcode_filename_without_extension(self):
        return f"barcode_{self.short_card_number}"

    @property
    def barcode_filename_with_extension(self):
        return f"{self.barcode_filename_without_extension}.svg"

    @property
    def barcode_fullpath_without_extension(self):
        return settings.STATICFILES_DIRS[0] / "svg" / self.barcode_filename_without_extension

    @property
    def barcode_fullpath_with_extension(self):
        return settings.STATICFILES_DIRS[0] / "svg" / self.barcode_filename_with_extension

    @property
    def barcode_path_for_template(self):
        return f"{settings.STATIC_URL}svg/{self.barcode_filename_with_extension}"
