from django.contrib import admin
from cyclediary.models import Cyclediary


@admin.register(Cyclediary)

class CyclediaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'diary_dt')
    list_filter = ('diary_dt', 'modify_dt')
    list_display_links = ['id', 'title']
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

