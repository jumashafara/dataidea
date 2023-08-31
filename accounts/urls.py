from django.contrib import admin
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path(route="signup", view=views.signup, name="signup"),
    path(route="signin", view=views.signin, name="signin"),
    path(route="signout", view=views.signout, name="signout")
]
