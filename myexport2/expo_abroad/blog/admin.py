from django.contrib import admin

# Register your models here.
from blog.models import Post, Category,Comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','description',]
	prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
	list_display=['title','status']
	prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
	list_display =['name','email','website']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)