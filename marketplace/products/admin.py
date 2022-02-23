from django.contrib import admin

from marketplace.products.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'quantity', 'owner')
    search_fields = ('name', 'owner')
    list_filter = ('is_active', )