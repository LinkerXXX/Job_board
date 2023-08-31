from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Specialization, Company, Vacancy, User, Application, Summary
from django.views import View
from board.forms import (
    UserCreateForm,
    UserAuthForm,
    ApplicationMessageForm,
    CompanyCreateForm,
    SearchForm,
)
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q



# https://docs.djangoproject.com/en/4.2/ref/forms/api/#initial-form-values


class VacancyDetailView(DetailView):
    template_name = "board/vacancy_detail.html"
    queryset = Vacancy.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = ApplicationMessageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ApplicationMessageForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = self.get_object()
            application.user = self.request.user
            application.save()
        return redirect("vacancies")


class IndexView(View):
    template_name = "board/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        all_company = Company.objects.all()
        all_specialization = Specialization.objects.all()
        all_vacancy = Vacancy.objects.all()
        context = {"companies": all_company, "specializations": all_specialization, "vacancies": all_vacancy}
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


########################################################


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = "account/create_user.html"
    success_url = "/vacancies/"


class UserAuthView(LoginView):
    form_class = UserAuthForm
    template_name = "account/auth.html"
    next_page = "/vacancies/"


class LogoutView(LogoutView):
    next_page = "main_page"


# https://github.com/django/django/blob/main/django/views/generic/edit.py#L185


##########################################


class CompanyDetailVacanciesView(View):
    template_name = "board/mycompany_detail_vacancies.html"

    def get(self, request, *args, **kwargs):
        company = request.user.companies.first()
        if request.user.is_authenticated and company:
            return render(request, self.template_name, {"company": company})
        else:
            return render(request, "account/auth.html")

class CompanyDetailView(View):
    template_name = "board/mycompany_detail.html"

    def get(self, request, *args, **kwargs):
        company = request.user.companies.first()
        if request.user.is_authenticated and company:
            return render(request, self.template_name, {"company": company})
        elif request.user.is_authenticated and not company:
            return render(request, "board/create_company.html")
        else:
            return render(request, "account/auth.html")


class CompanyCreateView(CreateView):
    template_name = "board/create_company.html"
    queryset = Company.objects.all()
    fields = ["name", "city", "logo", "description", "employee_count"]
    success_url = reverse_lazy("mycompany")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
#reverse("mycompany_creation")

class CompanyUpdateView(UpdateView):
    queryset = Company.objects.all()
    fields = ["name", "city", "logo", "description", "employee_count"]
    template_name = "board/update_company.html"
    success_url = "/mycompany/"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        print(queryset)
        return queryset


class VacancyUpdateView(UpdateView):
    queryset = Vacancy.objects.all()
    fields = ["name", "specialization", "skills", "description", "salary_max", "salary_min"]
    template_name = "board/update_vacancy.html"
    success_url = "/mycompany/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(company__owner=self.request.user)
    


class VacancyCreateView(CreateView):
    template_name = "board/create_vacancy.html"
    queryset = Vacancy.objects.all()
    fields = ["name", "specialization", "skills", "description", "salary_max", "salary_min"]
    success_url = reverse_lazy("mycompany")

    def form_valid(self, form):
        company = Company.objects.filter(owner=self.request.user).first()
        form.instance.company = company
        return super().form_valid(form)
    


    ##################################################################################################

class SummaryCreateView(CreateView):
    template_name = "board/create_summary.html"
    queryset = Summary.objects.all()
    fields = ["name", 'skills', "information", "contacts"]
    success_url = "/vacancies/"
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
    
class SummaryDetailView(CreateView):
    template_name = "board/mysummary_detail.html"

    def get(self, request, *args, **kwargs):
        summary = request.user.summary.first()
        if request.user.is_authenticated and summary:
            return render(request, self.template_name, {"summary": summary})
        elif request.user.is_authenticated and not summary:
            return render(request, "board/create_summary.html")
        else:
            return render(request, "account/auth.html")
        

class SummaryUpdateView(UpdateView):
    queryset = Summary.objects.all()
    fields = ["name", "skills", "information", "contacts"]
    template_name = "board/mysummary_update.html"
    success_url = "/mysummary_detail/"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    

#########################################################

class VacancySearchView(ListView):
    model = Vacancy
    template_name = 'board/index.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Vacancy.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
    
    