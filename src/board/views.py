from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Specialization, Company, Vacancy, User, Application
from django.views import View
from board.forms import UserCreateForm, UserAuthForm, ApplicationMessageForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView


# https://docs.djangoproject.com/en/4.2/ref/forms/api/#initial-form-values
class VacancyDetailView(DetailView):
    template_name = "board/vacancy_detail.html"
    queryset = Vacancy.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_app"] = ApplicationMessageForm(initial={"vacancy": context["vacancy"], "user": self.request.user})
        return context

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


########################################################

class CreateUserView(CreateView):
    form_class = UserCreateForm 
    template_name = 'account/create_user.html' 
    success_url = '/vacancies/'

class UserAuthView(LoginView):
    form_class = UserAuthForm
    template_name = 'account/auth.html'
    next_page = '/vacancies/'

class LogoutView(LogoutView):
    next_page = "main_page"


class ApplicationMessageView(CreateView):
    form_class = ApplicationMessageForm
    template_name = 'includes/interview.html'
    success_url = '/'

# https://github.com/django/django/blob/main/django/views/generic/edit.py#L185
    



    