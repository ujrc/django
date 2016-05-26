from django.conf.urls import url
from contacts import views as contact_view
from contacts.views import ContactUpdate
contact_urls =[
	url(r'^$',contact_view.contact_detail,name='contact_detail'),
	url(r'^edit/$',ContactUpdate.as_view(),name='contact_update'),
]