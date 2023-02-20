from django.shortcuts import render
from django.views.generic import ListView
from board.models import Specialization, Company

# Create your views here.

#class SpecializationListView(ListView):
#    queryset = Specialization.objects.all()
#    template_name = 'board/main_info.html'
#
#
#class CompanyListView(ListView):
#    queryset = Company.objects.all()
#    template_name = 'board/main_info.html'


def get_board_info(request):
    template_name = 'board/base.html'
    all_company = Company.objects.all()
    all_specialization = Specialization.objects.all()
    context = {"company": all_company}
    return render(request, template_name, context)