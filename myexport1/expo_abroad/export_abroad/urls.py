"""export_abroad URL Configuration

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
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.views.generic import TemplateView

from contact import views
from homepage import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name="homepage/main.html"), name='mainpage'),
    # url(r'^main/',views.HomePageView.as_view(),name='home'), 
    url(r'^home/',include('homepage.urls',namespace='homepage')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/',include('contact.urls')), 
    url(r'^users/',include('myuser.urls',namespace='myuser')), 
    url(r'^blog/',include('blog.urls')),
    # url(r'^accounts/login/$',login,{'template_name':'accounts/login.html'},name='login'),
    # url(r'^accounts/logout/$',logout,{'template_name':'accounts/logout.html'},name='logout'),#,'next_page':'/login/'}},name='logout'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)