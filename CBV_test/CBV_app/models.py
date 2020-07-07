from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=250)
    Domain = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CBV_app:details',kwargs={'pk':self.pk})

class Employees(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='Employees')

    def __str__(self):
        return self.name


