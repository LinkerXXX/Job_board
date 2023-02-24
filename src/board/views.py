from django.shortcuts import render
from django.views.generic import ListView
from board.models import Specialization, Company, Vacancy

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
    context = {"companies": all_company, 'specializations': all_specialization}
    return render(request, template_name, context)


from django.views import View

class IndexView(View):
    template_name = 'board/base.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)


    def get_context_data(self, *args, **kwargs):
        # context = super().get_context_data(*args, **kwargs)
        all_company = Company.objects.all()
        all_specialization = Specialization.objects.all()
        context = {"companies": all_company, 'specializations': all_specialization}
        return context
        

