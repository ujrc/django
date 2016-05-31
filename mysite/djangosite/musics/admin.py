from django.contrib import admin

# Register your models here.

from .models import Album,Song

class AlbumAdmin(admin.ModelAdmin):
	"""docstring for AlbumAdmin"""
	list_display= ['album_title','artist','user']
	list_filter=['user']


admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)