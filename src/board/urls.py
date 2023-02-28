from django.urls import path

# from board.views import get_board_info
from board.views import IndexView, VacancyListView, SpecializationListView, CompanyListView

urlpatterns = [
    # path("all/", get_board_info, name="main_page")
    path("", IndexView.as_view(), name="main_page"),
    path("vacancy_list/", VacancyListView.as_view(), name="vacancy_page"),
    path("spec_list/<int:pk>/",SpecializationListView.as_view(), name = "vacancy_spec_page"),
    path("company_list/<int:pk>/",CompanyListView.as_view(), name= "company_page")
]