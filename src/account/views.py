from django.shortcuts import render
from account.forms import UserCreateForm, UserAuthForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = "account/create_user.html"
    success_url = "/vacancies/"


class UserAuthView(LoginView):
    form_class = UserAuthForm
    template_name = "account/auth.html"
    next_page = "/vacancies/"


class LogoutView(LogoutView):
    next_page = "/vacancies/"
