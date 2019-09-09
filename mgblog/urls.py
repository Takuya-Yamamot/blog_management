from django.urls import path
from . import views

app_name = "mgblog"
urlpatterns = [
    path("", views.index, name="index"),
    path("breif/<int:clientId>", views.breif, name="breif"),
    path("plan_form", views.plan_form, name="plan_form"),
]
