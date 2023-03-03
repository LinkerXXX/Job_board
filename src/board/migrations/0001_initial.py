# Generated by Django 4.1.4 on 2022-12-29 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                        upload_to="MEDIA_COMPANY_IMAGE_DIR",
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
                        upload_to="MEDIA_SPECIALITY_IMAGE_DIR",
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
                    "discription",
                    models.TextField(max_length=1023, verbose_name="Описание вакансии"),
                ),
                (
                    "salary_max",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Верхний предел зарплаты",
                    ),
                ),
                (
                    "salary_min",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Нижний предел зарплаты",
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
    ]
