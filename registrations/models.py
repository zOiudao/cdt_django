from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da empresa")

    def __str__(self):
        return self.name


class Sector(models.Model):
    sector_name = models.CharField(max_length=255, verbose_name="Setor")
    extension = models.PositiveIntegerField(verbose_name="Ramal")

    def __str__(self):
        return self.sector_name


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    functional = models.PositiveIntegerField()
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.SET_NULL, null=True, blank=True
    )
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
