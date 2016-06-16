from django.contrib import admin

# Register your models here.
from .models import Course,Module,Subject

class SubjectAdmin(admin.ModelAdmin):
	list_display =['name','slug']
	prepopulated_fields ={'slug':['name']}

admin.site.register(Subject,SubjectAdmin)

class ModuleInline(admin.StackedInline):
	model=Module

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
	ist_display = ['title', 'subject', 'created']
	list_filter = ['created_on', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('name',)}
	inlines = [ModuleInline]
