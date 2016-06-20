from django.conf.urls import url
from django.contrib.auth.views import login,logout

from myuser import views
# app_name='myuser'
urlpatterns=[
	url(r'^login/$',login,{'template_name':'myuser/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'myuser/logout.html'},name='logout'),

	url(r'^register/$',views.UserRegistrationView.as_view(),name='register'),
	url(r'^users/(?P<slug>[-\w]+)/$', views.UserProfileDetailView.as_view(),name='profile'),
	url(r'^edit_profile/$', views.UserProfileUpdateView.as_view(), name='edit_profile'),
	]