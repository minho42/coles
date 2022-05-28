from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("profiles:user", kwargs={})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        self.email = BaseUserManager.normalize_email(self.email)
        super().save(*args, **kwargs)

    @property
    def firstname_or_username(self):
        if self.first_name:
            return self.first_name
        return self.username

    @property
    def initial(self):
        initial = ""
        if len(self.first_name) > 0:
            initial = self.first_name[0]
        if len(self.last_name) > 0:
            initial += self.last_name[0]

        if not (self.first_name or self.last_name):
            initial = self.username[0]
        return initial
