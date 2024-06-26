from django.contrib import admin

from .models import Transaction, TransactionItem


# Register your models here.
class TansactionIteminline(admin.TabularInline):
    model = TransactionItem
    extra = 0


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'created', 'updated', 'total']
    list_filter = ['status', 'created', 'updated']
    search_fields = ['id', 'status', 'created', 'updated']

    inlines = [TansactionIteminline]

    def total_price(self, obj):
        return obj.total_price()


register = admin.site.register(Transaction, TransactionsAdmin)
