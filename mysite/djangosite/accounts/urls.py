from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'accounts/logout.html'}, name='logout'),
]
