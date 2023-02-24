from django.urls import path

# from board.views import get_board_info
from board.views import IndexView

urlpatterns = [
    # path("all/", get_board_info, name="main_page")
    path("", IndexView.as_view(), name="main_page")

]