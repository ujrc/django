from django.conf.urls import url

from .views import CommCreateView, CommDeleteView, CommDetailView, CommListView, CommUpdateView

urlpatterns = [
    # url(r'^$'CommDetailView.as_view(),namw='comm_detail'),
    url(r'^$', CommListView.as_view(), name='comm_list'),
    url(r'^new/(?P<client_id>[0-9]+)/$',
        CommCreateView.as_view(), name='comm_new'),
    url(r'^edit/(?P<pk>[0-9]+)/$', CommUpdateView.as_view(), name='comm_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$',
        CommDeleteView.as_view(), name='comm_delete'),
]
