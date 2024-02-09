from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Korzina)
class AdminKorzina(admin.ModelAdmin):
    list_display = ('user','tovar','count','summa')