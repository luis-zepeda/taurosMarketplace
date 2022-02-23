from django.contrib import admin
from jmespath import search

from marketplace.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_diplay = ('amount', 'product', 'buyer', 'seller')
    search_fields = ('amount', 'product', 'buyer', 'seller')
