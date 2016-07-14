
from django.conf.urls import url

from .views import (ContactCreateView, ContactDeleteView,
                    ContactListView, ContactUpdateView)  # ContactDetailView

urlpatterns = [
    url(r'^$', ContactListView.as_view(), name='contact_list'),
    url(r'^new/(?P<client_id>[0-9]+)/$',
        ContactCreateView.as_view(), name='contact_new'),
    url(r'^edit/(?P<pk>[0-9]+)/$',
        ContactUpdateView.as_view(), name='contact_edit'),
    url(r'^(?P<pk>\d+)/delete/$', ContactDeleteView.as_view(), name='contact_delete'),
    # url(r'^(?P<slug>[\-w]+)/$',contact_detail,name='contact_detail'),
    # url(r'^(?P<pk>[0-9]+)/$',ContactDetailView.as_view(),name='contact_detail'),
]

