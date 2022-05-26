from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [path("<slug:slug>/", views.profile, name="user")]
