"""djangosite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login,logout
from djangosite.views import HomePageView


urlpatterns = [
    url(r'^$',HomePageView.as_view(),name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/',include('musics.urls')),
    url(r'^login/$',login,{'template_name':'registration/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'registration/logout.html','next_page':'/login/'},name='logout'),

 
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

