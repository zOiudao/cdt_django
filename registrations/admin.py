from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Employee)
admin.site.register(models.Sector)
admin.site.register(models.Enterprise)
