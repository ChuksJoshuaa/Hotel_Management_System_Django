from django.contrib import admin
from .models import Rooms, Booking, Contact, News

admin.site.register(News)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'user_id', 'start_day', 'end_day']
    list_per_page = 5
    list_filter = ['room_no']
    search_fields = ['room_no']


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['manager', 'room_no', 'room_type', 'price']
    actions = ['clear_price']
    list_per_page = 5
    list_editable = ['price', 'room_no']
    list_filter = ['manager', 'room_no']
    search_fields = ['manager', 'room_type']

    @admin.action(description='Clear price')
    def clear_price(self, request, queryset):
        updated_count = queryset.update(price=0)
        self.message_user(
            request,
            f'{updated_count} rooms were successfully updated'
        )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_per_page = 5
    list_filter = ['name']
    search_fields = ['name']