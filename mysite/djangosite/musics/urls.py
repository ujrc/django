from django.conf.urls import url

from .import views
from django.contrib.auth.views import login,logout

app_name='musics'
urlpatterns=[
url(r'^$',views.HomeView.as_view(),name='home'),
url(r'^register/$',views.UserFormView.as_view(),name='register'),
url(r'^login/$',login,{'template_name':'registration/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'registration/logout.html','next_page':'/login/'},name='logout'),
url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),

url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

url(r'^album/(?P<pk>\d+)/$',views.AlbumDelete.as_view(),name='album-delete'),

# url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]