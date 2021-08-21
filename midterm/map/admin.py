from django.contrib import admin
from map.models import Map

# Register your models here.

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'url')
    list_display_links = ['id', 'title']