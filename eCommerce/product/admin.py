from django.contrib import admin
from product.models import Product, ProductDetail, ProductStock, ProductTag

# Register your models here.


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'image', 'current_stock']
    list_per_page = 30

    def current_stock(self, obj):
        return obj.current_stock()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'product_tags',
        'created',
        'updated',
        'active',
    ]
    list_per_page = 30

    def product_tags(self, obj):
        return obj.product_tag.name


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    list_per_page = 30


@admin.register(ProductStock)
class ProductStock(admin.ModelAdmin):
    list_display = ['id', 'product', 'amount', 'status', 'created_by', 'created', 'updated']
    list_per_page = 30
