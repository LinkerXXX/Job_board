from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Specialization, Company, Vacancy
from django.views import View


class IndexView(View):
    template_name = "board/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        all_company = Company.objects.all()
        all_specialization = Specialization.objects.all()
        context = {"companies": all_company, "specializations": all_specialization}
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
