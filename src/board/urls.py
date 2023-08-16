from django.urls import path

from board.views import (
    IndexView,
    VacancyListView,
    SpecializationListView,
    CompanyListView,
    VacancyDetailView,
    CreateUserView,
    UserAuthView,
    LogoutView,
    CompanyDetailVacanciesView,
    CompanyDetailView,
    CompanyCreateView,
    CompanyUpdateView,
    VacancyUpdateView,
    VacancyCreateView,
    SummaryCreateView,
    SummaryDetailView,
    SummaryUpdateView
)
from account.views import CreateUserView

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
    path("register/", CreateUserView.as_view(), name="createUser"),
    path("login/", UserAuthView.as_view(), name="authUser"),
    path("logout/", LogoutView.as_view(), name="logoutUser"),
    path(
        "mycompany/vacancies/",
        CompanyDetailVacanciesView.as_view(),
        name="mycompany_vacancies",
    ),
    path("mycompany/", CompanyDetailView.as_view(), name="mycompany"),
    path("mycompany_creation/", CompanyCreateView.as_view(), name="mycompany_creation"),
    path(
        "mycompany_update/<int:pk>/",
        CompanyUpdateView.as_view(),
        name="mycompany_update",
    ),
    path(
        "myvacancy_update/<int:pk>/",
        VacancyUpdateView.as_view(),
        name="myvacancy_update",
    ),
    path("myvacancy_creation/", VacancyCreateView.as_view(), name="myvacancy_creation"),
    path("mysummary_creation/", SummaryCreateView.as_view(), name="mysummary_creation"),
    path("mysummary_detail/", SummaryDetailView.as_view(), name="mysummary_detail"),
    path("mysummary_update/<int:pk>/", SummaryUpdateView.as_view(), name="mysummary_update"),
]
