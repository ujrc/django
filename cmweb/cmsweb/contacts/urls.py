from django.conf.urls import url
from contacts import views as contact_view
contact_urls =[
	url(r'^$',contact_view.contact_detail,name='contact_detail'),
	url(r'^edit/$',contact_view.contact_create,name='contact_update'),
]