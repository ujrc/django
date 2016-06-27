from django.conf.urls import url, include

from .import views
from django.contrib.auth.views import login, logout

albums_urls = [
    url(r'^$', views.AlbumListView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^a/create/$', views.AlbumCreate.as_view(), name='album_create'),
    url(r'^(?P<slug>[-\w]+)/update/$',
        views.AlbumUpdate.as_view(), name='album_edit'),
    url(r'^(?P<slug>[-\w]+)/delete/$',
        views.AlbumDeleteView.as_view(), name='album_delete'),

    # url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]

songs_urls = [
    url(r'^$', views.SongListView.as_view(), name='song_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.SongDetailView.as_view(), name='song_detail'),
    url(r'^s/create_song/$', views.SongCreateView.as_view(), name='song_create'),
    url(r'^(?P<slug>[-\w]+)/update_song/(?P<song_slug>[-\w]+)/$',
        views.SongUpdateView.as_view(), name='song_edit'),
    url(r'^(?P<slug>[-\w]+)/delete_song/(?P<song_slug>[-\w]+)/$',
        views.SongDeleteView.as_view(), name='song_delete'), ]

urlpatterns = [
    url(r'^album/',include(albums_urls, namespace='albums')),
    url(r'^song/', include(songs_urls, namespace='songs')),
]
