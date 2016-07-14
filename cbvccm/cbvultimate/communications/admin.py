# Register your models here.
from django.contrib import admin

from .models import Communication


class CommAdmin(admin.ModelAdmin):
    list_display = ['subject', 'kind']

admin.site.register(Communication, CommAdmin)
