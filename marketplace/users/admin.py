from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Wallet


@admin.register(User)
class UserAdmin(UserAdmin):
    
    list_display = ('id', 'username', 'email', 'is_staff', 'is_seller', 'is_admin')
    list_filter = ('is_seller', 'is_staff', 'is_admin', 'created', 'modified')


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    
    list_display = ('balance', 'user')
    search_fields = ('user', )