from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length = 50)
    
    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        
    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    info = models.TextField(max_length=1023)
    staff = models.TextField(max_length=1023)
    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.ManyToManyField(Specialization, null=True, blank=True, related_name="vacancies") 
    company = models.ForeignKey(Company, null=True, blank=True, related_name="vacancies")
    skills = models.TextField(max_length=1023)
    discription = models.TextField(max_length=1023)
    money_down = models.CharField(max_length=50, blank=True, null=True)
    money_up = models.CharField(max_length=50, blank=True, null=True)
    data_creation = models.DateTimeField(auto_now=True)
    data_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-data_creation"]
        
    def __str__(self):
        return self.name
        
    