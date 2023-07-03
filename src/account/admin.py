from django.contrib import admin
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "birthday",
        "email",
        "id"
    )
    search_fields = ("^company",)
    list_filter = ("first_name", "last_name")
    ordering = ("username",)
    readonly_fields = ("birthday",)
