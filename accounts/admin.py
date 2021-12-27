from django.contrib import admin
from .models import Manager, Customer


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_no']
    list_editable = ['email', 'phone_no']
    list_filter = ['username']
    list_per_page = 5
    search_fields = ['username', 'email']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_no']
    list_editable = ['email', 'phone_no']
    list_per_page = 5
    search_fields = ['username', 'email']


