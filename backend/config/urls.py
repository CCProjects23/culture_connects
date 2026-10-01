"""URL configuration for the Culture Connects backend."""

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", views.api_root, name="api-root"),
    path("api/health", views.health, name="health"),
    path("api/health/", views.health),
]
