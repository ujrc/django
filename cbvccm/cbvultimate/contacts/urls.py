#contacts/urls.py
from django.conf.urls import url

from .views import  (ContactCreateView,ContactDeleteView,ContactDetailView,
	ContactListView,ContactUpdateView)

urlpatterns=[
url(r'^$',ContactListView.as_view(),name='contact_list'),
url(r'^new/(?P<client_id>[0-9]+)/$',ContactCreateView.as_view(),name='contact_new'),
# url(r'^(?P<slug>[\-w]+)/$',contact_detail,name='contact_detail'),
url(r'^(?P<slug>[\-w]+)/$',ContactDetailView.as_view(),name='contact_detail'),
url(r'^(?P<slug>[\-w]+)/edit/$',ContactUpdateView.as_view(),name='contact_edit'),
url(r'^(?P<slug>[\-w]+)/delete/$',ContactDeleteView.as_view(),name='contact_delete'),
]