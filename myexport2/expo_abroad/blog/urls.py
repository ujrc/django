from django.conf.urls import url
from . import views
app_name='blog'
urlpatterns=[
	url(r'^$',views.CategoryListView.as_view(),name='category_list'),
	url(r'^add/$',views.CategoryCreateView.as_view(),name='category_create'),
	url(r'^category/(?P<slug>[-\w]+)/$',views.CategoryDetailView.as_view(),name='category_detail'),
	url(r'^edit/(?P<slug>[-\w]+)/$',views.CategoryUpdateView.as_view(),name='category_edit'),
	url(r'^delete/(?P<slug>[-\w]+)/$',views.CategoryDeleteView.as_view(),name='category_delete',),
	url(r'^post/(?P<slug>[-\w]+)/$',views.PostDetailView.as_view(),name='post_detail'),

]