from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from board.models import User, Application, Company
from django.forms import ModelForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")


class ApplicationMessageForm(ModelForm):
    class Meta:
        model = Application
        fields = ["name", "phone", "covering_letter"]


class CompanyCreateForm(ModelForm):
    class Meta:
        model = Company
        fields = ["name", "city", "logo", "description", "employee_count"]

class SearchForm(forms.Form):
    query = forms.CharField()
