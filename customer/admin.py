from django.contrib import admin

from .models import Address, Customer, CustomerCoupon


class CustomerCouponInlineAdmin(admin.TabularInline):
    model = CustomerCoupon
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_per_page = 20

    inlines = [CustomerCouponInlineAdmin]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_per_page = 20
