from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Car,CarAdmin

admin.site.register(Car, CarAdmin)