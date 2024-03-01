from django.contrib import admin

from .models import Address, Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_per_page = 20


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_per_page = 20
