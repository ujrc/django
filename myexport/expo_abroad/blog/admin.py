from django.contrib import admin

# Register your models here.
from blog.models import Post, Category,Comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','description',]
	prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
	list_display=[ 'author','title','content','created','status','published','category']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['status', 'created', 'published', 'author']
	search_fields = ['title', 'content']
	# raw_id_fields = ('author',)
	date_hierarchy = 'published'
	ordering = ['status', 'published']


class CommentAdmin(admin.ModelAdmin):
	list_display =['name','email','website']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)