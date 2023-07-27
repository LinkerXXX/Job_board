from django.urls import path
from account.views import CreateUserView, UserAuthView, LogoutView

urlpatterns = [
    path("create/", CreateUserView.as_view()),
    path("auth/", UserAuthView.as_view()),
    path("logout/", LogoutView.as_view()),
]
