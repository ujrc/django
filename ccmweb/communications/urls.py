from django.conf.urls import patterns, url
from communications import views as comm_view
comm_urls = [
	url(r'^$',comm_view.comm_detail, name="comm_detail"),
]