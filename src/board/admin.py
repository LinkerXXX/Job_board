from django.contrib import admin
from board.models import Vacancy, Company, Specialization


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialization",
        "company",
        "skills",
        "description",
        "salary_max",
        "salary_min",
    )
    search_fields = ("^company",)
    list_filter = (
        "created_at",
        "specialization",
    )
    ordering = ("updated_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "description", "employee_count")
    search_fields = ("^name",)
    list_filter = ("city",)
    ordering = ("name",)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("^name",)
    list_filter = ("name",)
    ordering = ("name",)
