"""ccmweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as django_view
from marketing.views import HomePage
from subscribers import views as subscribers_view

from accounts.views import AccountList
from accounts import views as accounts_view
from accounts.urls import account_urls
from communications.views import CommDelete
from communications.urls import comm_urls
from communications import views as comm_view
from contacts.views import ContactDelete, ContactCreate,UpdateView
from contacts import views as contacts_view
from contacts.urls import contact_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage.as_view(),name='home'),

    # Subscribers URL
    url(r'^signup/$',subscribers_view.subscriber_new,name='sub_new'),
    url(r'^login/$',django_view.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$',django_view.logout,{'next_page':'/login/'},name='logout'),
    # Account related URLs
    
    url(r'^account/new/$',accounts_view.account_cru,name='account_new'),
    url(r'^account/list/$',AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/',include(account_urls)),

    # Contact related  URLs

    url(r'^contact/new/$',ContactCreate.as_view(), name='contact_new'),
    url(r'^contact/(?P<uuid>[\w-]+)/',include(contact_urls)),
    url(r'^contact/(?P<pk>\d+)/delete/$',ContactDelete.as_view(),
     name='contact_delete'),

 # Communication related URLs
    url(r'^comm/new/$',comm_view.comm_cru, name='comm_new'),
    url(r'^comm/(?P<uuid>[\w-]+)/',include(comm_urls)),
    url(r'^comm/(?P<pk>[\w-]+)/delete/$', CommDelete.as_view(),
     name='comm_delete'),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

