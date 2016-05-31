from django.conf.urls import url

from .import views
from django.contrib.auth.views import login,logout

app_name='musics'
urlpatterns=[
url(r'^$',views.HomeView.as_view(),name='home'),
url(r'^register/$',views.UserFormView.as_view(),name='register'),
url(r'^(?P<slug>[-\w]+)/$',views.DetailView.as_view(),name='detail'),
url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),
url(r'^album/(?P<slug>[-\w]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
url(r'^album/(?P<slug>[-\w]+)/delete/$',views.AlbumDeleteView.as_view(),name='album-delete'),
url(r'^songs/(?P<slug>[-\w]+)/$',views.SongDetailView.as_view(), name='songs'),

# url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]