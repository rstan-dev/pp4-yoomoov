from django.contrib import admin
from .models import Van


@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'location', 'crew', 'date_added', 'is_live')
