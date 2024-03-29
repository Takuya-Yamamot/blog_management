from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views
from .views import index, breif, plan_form, plan_list, breif_form

app_name = "mgblog"
urlpatterns = [
    path("", index, name="index"),
    path("breif/<int:clientId>/", breif, name="breif"),
    path("plan_form", plan_form, name="plan_form"),
    path("plan_list/<int:clientId>/", plan_list, name="plan_lists"),
    path("breif_form", breif_form, name="breif_form"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logged_out/", views.LogoutView.as_view(), name="logged_out"),
    path("auth", include("social_django.urls", namespace="social")),
]
