from django.urls import path

from board.views import get_board_info

urlpatterns = [
    path("all/", get_board_info, name="main_page")
]