from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus


def page_404_view(request, exception):
    return render(request, "404.html", status=HTTPStatus.NOT_FOUND)


def page_500_view(request):
    return render(request, "500.html", status=HTTPStatus.INTERNAL_SERVER_ERROR)
