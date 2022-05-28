from django.urls import path

from . import views

app_name = "coles"

urlpatterns = [
    path("", views.ColesListView.as_view(), name="list"),
    path("add/", views.ColesCreateView.as_view(), name="add"),
    path("<int:pk>", views.ColesDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.ColesDeleteView.as_view(), name="delete"),
    path("sync/", views.sync, name="sync"),
]
