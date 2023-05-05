from django.urls import path

from board.views import (
    IndexView,
    VacancyListView,
    SpecializationListView,
    CompanyListView,
    VacancyDetailView,
    CreateUserView,
    UserAuthView,
    LogoutView
)

urlpatterns = [
    path("", IndexView.as_view(), name="main_page"),
    path("vacancies/", VacancyListView.as_view(), name="vacancies"),
    path(
        "vacancies/<str:slug>/",
        SpecializationListView.as_view(),
        name="specializations",
    ),
    path("companies/<int:pk>/", CompanyListView.as_view(), name="companies"),
    path("vacancy/<int:pk>/", VacancyDetailView.as_view(), name="vacancy"),
    path("register/",CreateUserView.as_view(), name="createUser"),
    path("login/", UserAuthView.as_view(), name="authUser"),
    path("logout/", LogoutView.as_view(), name="logoutUser"),
]
