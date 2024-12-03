from django.urls import path
from .views import SignUp, login_view, logout_view
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


