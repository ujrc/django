from django.contrib import admin
from contact.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	class Meta:
		model=Contact
admin.site.register(Contact,ContactAdmin)