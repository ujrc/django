from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','uuid']

admin.site.register(Contact,ContactAdmin)