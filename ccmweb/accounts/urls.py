from django.conf.urls import url

account_urls=[
	url(r'^S','accounts.views.account_detail',name='account_detail'),

]