from django.conf.urls import url
from .views import (MainPage, AboutView,
                    ContactUsView, PrivacyView, CopyRightView, TermsView
                    )

urlpatterns = [

    # Main page
    url(r'^$', MainPage.as_view(), name='mainpage'),
    # url(r'^main/$',TemplateView.as_view(),name='mainpage'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contactus/$', ContactUsView.as_view(), name='contactus'),
    url(r'^terms/$', TermsView.as_view(), name='terms'),
    url(r'^copyright$', CopyRightView.as_view(), name='copyright'),
    url(r'^privacy/$', PrivacyView.as_view(), name='privacy'),

]
