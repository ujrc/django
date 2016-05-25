from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Communication

class CommunicationAdmin(admin.ModelAdmin):
	list_display=['subject','uuid']

admin.site.register(Communication,CommunicationAdmin)