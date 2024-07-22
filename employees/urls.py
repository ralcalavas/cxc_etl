from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("charge_catalog", views.charge_catalog, name="catalog"),
    path("charge_employees", views.charge_employees, name="catalog"),
]