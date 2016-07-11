from django.conf.urls import url
from .views import ClientListView,ClientDetailView, ClientCreateView, ClientDeleteView,ClientUpdateView

urlpatterns=[

    url(r'^$',ClientListView.as_view(), name='client_list'),
	url(r'^new/$',ClientCreateView.as_view(),name='client_new'),
    url(r'^(?P<slug>[\w-]+)/$',ClientDetailView.as_view(),name='client_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$',ClientUpdateView.as_view(),name='client_edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$',ClientDeleteView.as_view(),name='client_delete'),
]