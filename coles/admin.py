from django.contrib import admin

from core.utils import get_all_fields_excluding, get_all_fields

from .models import Coles


class ColesAdmin(admin.ModelAdmin):
    list_display: get_all_fields_excluding(Coles, [])


admin.site.register(Coles, ColesAdmin)
