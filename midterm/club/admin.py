from django.contrib import admin
from club.models import Club


@admin.register(Club)

class Club(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt', 'riding_dt')
    list_filter = ('riding_dt', 'modify_dt')
    list_display_links = ['id', 'name']
    search_fields = ('name', 'content', 'city', 'location')
