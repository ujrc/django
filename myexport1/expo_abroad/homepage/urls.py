from django.conf.urls import url,include
from homepage import views
urlpatterns=[
	url(r'^$', views.HomePageView.as_view(), name ='home'), 
	 
]