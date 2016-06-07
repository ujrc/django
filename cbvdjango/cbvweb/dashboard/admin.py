from django.contrib import admin

# Register your models here.
from .forms import BookForm
from .models import Book
class BookAdmin(admin.ModelAdmin):
	list_display=['title','slug']
	readonly_fields =['modified','timestamp','added_by','last_edit_by']

	form = BookForm
admin.site.register(Book,BookAdmin)