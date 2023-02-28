from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Specialization, Company, Vacancy
from django.views import View
# Create your views here.

#class SpecializationListView(ListView):
#    queryset = Specialization.objects.all()
#    template_name = 'board/main_info.html'
#
#
#class CompanyListView(ListView):
#    queryset = Company.objects.all()
#    template_name = 'board/main_info.html'


#def get_board_info(request):
#    template_name = 'board/base.html'
#    all_company = Company.objects.all()
#    all_specialization = Specialization.objects.all()
#    context = {"companies": all_company, 'specializations': all_specialization}
#    return render(request, template_name, context)



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
        

class VacancyListView(ListView):
    template_name = "board/vacancy_list.html"
    queryset = Vacancy.objects.all()
    

class SpecializationListView(DetailView):
    template_name = "board/specialization_list.html"
    queryset = Specialization.objects.all()
    

class CompanyListView(DetailView):
    template_name = "board/company_list.html"
    queryset = Company.objects.all()

#    def get(self, request, *args, **kwargs):
#        context = self.get_context_data(*args, **kwargs)
#        return render(request, self.template_name, context)
#
#    def get_context_data(self, *args, **kwargs):
#        all_specialization = Specialization.objects.all()
#        all_vacancy = Vacancy.objects.all()
#        context = {'specializations': all_specialization, "vacancies":all_vacancy}
#        return context

#class  VacancyListView(View):
#    template_name = "board/vacancy_list.html"
#
#    def get(self, request, *args, **kwargs):
#        context = self.get_context_data(*args, **kwargs)
#        return render(request, self.template_name, context)
#
#
#    def get_context_data(self, *args, **kwargs):
#        all_company = Company.objects.all()
#        all_specialization = Specialization.objects.all()
#        all_vacancy = Vacancy.objects.all()
#        context = {"companies": all_company, 'specializations': all_specialization, "vacancies":all_vacancy}
#        return context