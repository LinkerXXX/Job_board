from django.db import models
from django.conf import settings


class Specialization(models.Model):
    name = models.CharField(
        max_length=50, blank=False, null=False, verbose_name="Название специализации"
    )
    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR,
        verbose_name="Логотип специализации",
    )
    slug = models.SlugField(max_length=50, verbose_name="Слаг специализации")

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        max_length=50, blank=False, null=False, verbose_name="Название компании"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to=settings.MEDIA_COMPANY_IMAGE_DIR,
        verbose_name="Логотип компании",
    )
    description = models.TextField(max_length=1023, verbose_name="Описание компании")
    employee_count = models.IntegerField(verbose_name="Численность сотрудников")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Название вакансии"
    )
    specialization = models.ForeignKey(
        Specialization,
        null=True,
        blank=True,
        related_name="vacancies",
        verbose_name="Специализация вакансии",
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        related_name="vacancies",
        on_delete=models.CASCADE,
        verbose_name="Принадлежность к компании",
    )
    skills = models.TextField(max_length=1023, verbose_name="Требуемые навыки")
    description = models.TextField(max_length=1023, verbose_name="Описание вакансии")
    salary_max = models.IntegerField(
        blank=True, null=True, verbose_name="Верхний предел зарплаты"
    )
    salary_min = models.IntegerField(
        blank=True, null=True, verbose_name="Нижний предел зарплаты"
    )
    created_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата размещения вакансии"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления вакансии"
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
