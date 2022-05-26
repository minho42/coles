from django.urls import path

from . import views

app_name = "coles"

urlpatterns = [
    path("", views.ColesListView.as_view(), name="list"),
    path("add/", views.ColesCreateView.as_view(), name="add"),
    path("<int:id>", views.ColesCreateView.as_view(), name="detail"),
    path("<int:id>/edit/", views.ColesUpdateView.as_view(), name="edit"),
    path("<int:id>/delete/", views.ColesDeleteView.as_view(), name="delete"),
    path("sync/", views.sync, name="sync"),
]
