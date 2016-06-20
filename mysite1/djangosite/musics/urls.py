from django.conf.urls import url

from .import views
from django.contrib.auth.views import login,logout

app_name='musics'
urlpatterns=[
url(r'^$',views.HomeView.as_view(),name='home'),
url(r'^register/$',views.UserFormView.as_view(),name='register'),
url(r'^(?P<slug>[-\w]+)/$',views.AlbumDetailView.as_view(),name='detail'),
url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),
url(r'^album/(?P<slug>[-\w]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
url(r'^album/(?P<slug>[-\w]+)/delete/$',views.AlbumDeleteView.as_view(),name='album-delete'),
url(r'^songs$',views.SongListView.as_view(), name='song_list'),
url(r'^songs/(?P<slug>[-\w]+)/(?P<slug_song>[-\w]+)/$',views.SongDetailView.as_view(), name='detail_song'),
url(r'^(?P<album_slug>[-\w]+)/create_song/$', views.SongCreateView.as_view(), name='create_song'),
url(r'^(?P<album_slug>[-\w]+)/update_song/(?P<song_slug>[-\w]+)/$', views.SongUpdateView.as_view(), name='update_song'),
url(r'^(?P<album_slug>[-\w]+)/delete_song/(?P<song_slug>[-\w]+)/$', views.SongDeleteView.as_view(), name='delete_song'),
# url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]