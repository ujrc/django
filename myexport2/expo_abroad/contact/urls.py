from django.conf.urls import url
from contact import views
app_name='contact'
urlpatterns=[
	# url(r'^$',views.contact, name='contact'),
	url(r'^$',views.ContactFormView.as_view(), name='contact'),

	]