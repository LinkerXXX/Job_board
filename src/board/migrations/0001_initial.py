# Generated by Django 4.1.5 on 2023-04-18 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Название компании"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/company/",
                        verbose_name="Логотип компании",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=1023, verbose_name="Описание компании"),
                ),
                (
                    "employee_count",
                    models.IntegerField(verbose_name="Численность сотрудников"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="companies",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
            },
        ),
        migrations.CreateModel(
            name="Specialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, verbose_name="Название специализации"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/specialization/",
                        verbose_name="Логотип специализации",
                    ),
                ),
                ("slug", models.SlugField(verbose_name="Слаг специализации")),
            ],
            options={
                "verbose_name": "Специализация",
                "verbose_name_plural": "Специализации",
            },
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Название вакансии",
                    ),
                ),
                (
                    "skills",
                    models.TextField(max_length=1023, verbose_name="Требуемые навыки"),
                ),
                (
                    "description",
                    models.TextField(max_length=1023, verbose_name="Описание вакансии"),
                ),
                (
                    "salary_max",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Верхний предел зарплаты"
                    ),
                ),
                (
                    "salary_min",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Нижний предел зарплаты"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата размещения вакансии"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата обновления вакансии"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="board.company",
                        verbose_name="Принадлежность к компании",
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="board.specialization",
                        verbose_name="Специализация вакансии",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Имя отклика")),
                (
                    "phone",
                    models.CharField(max_length=50, verbose_name="Номер телефона"),
                ),
                (
                    "covering_letter",
                    models.TextField(
                        max_length=1023, verbose_name="Сопроводительное письмо"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="board.vacancy",
                        verbose_name="Вакансии",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отклик",
                "verbose_name_plural": "Отклики",
            },
        ),
    ]
