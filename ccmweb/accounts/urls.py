from django.conf.urls import url
from  accounts import  views as account_view

account_urls=[
	url(r'^$',account_view.account_detail,name='account_detail'),
	url(r'^edit/$',account_view.account_cru,name='account_update'),

]