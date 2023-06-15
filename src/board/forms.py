from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from board.models import User, Application
from django.forms import ModelForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ApplicationMessageForm(ModelForm):
    class Meta:
        model = Application
        fields = ["name", "phone", "covering_letter"]