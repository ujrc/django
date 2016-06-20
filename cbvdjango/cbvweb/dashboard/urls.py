from django.conf.urls import url
from dashboard import views

urlpatterns=[
	url(r'^create/$',views.BookCreateView.as_view(),name='book_create'), 
    url(r'^$',views.BookListView.as_view(),name='book_list'),
    url(r'^(?P<slug>[-\w]+)/$',views.BookDetail.as_view(),name='book_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$',views.BookUpdateView.as_view(),name='book_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$',views.BookDeleteView.as_view(),name='book_delete'),
   
]