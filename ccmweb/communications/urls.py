<<<<<<< HEAD
from django.conf.urls import patterns, url
from communications import views as comm_view
comm_urls = [
	url(r'^$',comm_view.comm_detail, name="comm_detail"),
]
=======
from django.conf.urls import url

from communications import views as comm_view

comm_urls=[
	url(r'^$',comm_view.comm_detail,name='comm_detail'),
	url(r'^edit/$',comm_view.comm_cru,name='comm_update'),

	]
>>>>>>> master
