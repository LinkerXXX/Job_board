from django.urls import path

from board.views import (
    IndexView,
    VacancyListView,
    SpecializationListView,
    CompanyListView,
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
]