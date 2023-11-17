from django.urls import path
from medicSearch.views.AuthView import login_view, register_view, logout_view


urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
    path("logout", logout_view, name='logout')
]
