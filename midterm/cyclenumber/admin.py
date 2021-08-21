from django.contrib import admin
from cyclenumber.models import Cyclenumber
# Register your models here.


@admin.register(Cyclenumber)

class CyclenumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number')
    list_display_links = ['id', 'name']
    search_fields = ('name', 'number', 'brand', 'modelname')
