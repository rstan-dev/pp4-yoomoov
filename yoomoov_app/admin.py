from django.contrib import admin
from .models import Van


@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'location', 'crew', 'date_added', 'is_live')
    list_display_links = ('name',)
    list_filter = ('size', 'location', 'crew', 'date_added')
    list_editable = ('is_live',)
    search_fields = ('name', 'size', 'location', 'county')
