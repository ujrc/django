from django.conf.urls import url
from .import views

app_name='musics'
urlpatterns=[
url(r'^$',views.home,name='home'),
url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

]