from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from board.models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')