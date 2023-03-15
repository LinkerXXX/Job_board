from django.shortcuts import render
from django.http import HttpResponse


def page_404_view(request, exception):
    return render(request, '404.html', status=404)

def page_500_view(request):
    return render(request, '500.html')

