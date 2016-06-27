from django.contrib import admin

# Register your models here.

from .models import Album, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'file_type']
    prepopulated_fields = {'slug': ('song_title',)}


class AlbumAdmin(admin.ModelAdmin):
    """docstring for AlbumAdmin"""
    list_display = ['album_title', 'artist', 'user']
    list_filter = ['user']
    prepopulated_fields = {'slug': ('album_title',)}


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
