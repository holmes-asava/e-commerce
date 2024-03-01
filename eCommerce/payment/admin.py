from django.contrib import admin

from .models import Transactions

# Register your models here.

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'timestamp', 'updated']
    list_filter = ['status', 'timestamp', 'updated']
    search_fields = ['id', 'status', 'timestamp', 'updated']
    list_editable = ['status']

    class Meta:
        model = Transactions