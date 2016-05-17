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
from django.conf.urls import url
from django.contrib import admin
from marketing.views import HomePage
from subscribers import views as subscribers_view

from accounts.views import AccountList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage.as_view(),name='home'),
    url(r'^signup/$',subscribers_view.subscriber_new,name='sub_new'),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/login/'}),
    # Account related URLs
    url(r'^account/list/$',AccountList.as_view(), name='account_list'
),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

