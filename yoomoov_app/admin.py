from django.contrib import admin
from .models import Van, Booking, Feedback


@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'crew', 'date_added', 'is_live')
    list_display_links = ('name',)
    list_filter = ('size', 'location', 'crew', 'date_added')
    list_editable = ('is_live',)
    search_fields = ('name', 'size', 'location', 'county')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_number', 'date_required', 'first_name', 'last_name', 'van', 'van_size', 'van_location', 'status', 'price')
    list_display_links = ('booking_number',)
    readonly_fields = ('booking_number',)
    list_filter = ('date_required', 'van_location', 'status')
    list_editable = ('status', 'price')
    search_fields = ('booking_number', 'first_name', 'last_name', 'van_location', 'status')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('booking_number', 'van_name', 'title', 'rating', 'is_approved')
    list_display_links = ('title',)
    list_editable = ('is_approved',)
