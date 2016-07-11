# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, UserAddress


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['street_address', 'city', 'state', 'country']


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

admin.site.register(UserAddress, UserAddressAdmin)
