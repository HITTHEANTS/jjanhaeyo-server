from django.contrib import admin
from accounts.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number', 'phone_otp_secret', 'is_active', 'is_staff', 'is_superuser', 'date_joined')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'push_token', 'login_secret')


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
