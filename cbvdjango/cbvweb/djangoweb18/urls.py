"""djangoweb18 URL Configuration

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

from django.views.generic.base import TemplateView
from newsletter import views as newsletter_view
from . import views
from dashboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',newsletter_view.home,name='home'),
    url(r'^contact/$',newsletter_view.contact,name='contact'),
    # url(r'^about/$',views.about,name='about'),

    url(r'^book/',include('dashboard.urls', namespace='dashboard')),
    url(r'^about/$',views.DashboardTemplateView.as_view(),name='about'),
    url(r'^someview/$',views.MyView.as_view(template_name='about.html'),name='someview'),
    url(r'^accounts/',include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)