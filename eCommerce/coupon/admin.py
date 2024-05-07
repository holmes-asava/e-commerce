from coupon.models import Coupon, CouponCondition
from django.contrib import admin
from product.models import Product, ProductTag

# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'start_date', 'end_date', 'status']
    list_per_page = 30


class ProductInlineAdmin(admin.TabularInline):
    model = CouponCondition.product.through
    extra = 0


class ProductTagInlineAdmin(admin.TabularInline):
    model = CouponCondition.product_tag.through
    extra = 0


@admin.register(CouponCondition)
class CouponConditionAdmin(admin.ModelAdmin):
    list_per_page = 30
    fields = [
        'status',
    ]
    list_display = ['id', 'status']

    inlines = [ProductInlineAdmin, ProductTagInlineAdmin]
