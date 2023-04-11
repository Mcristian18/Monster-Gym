from django.contrib import admin
from .models import User
from. models import Monthly
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class UserAdminConfig(UserAdmin):

    # ordering = ('date_joined',)
    # list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff')

# admin.site.register(User, UserAdminConfig)

admin.site.register(User)
admin.site.register(Monthly)