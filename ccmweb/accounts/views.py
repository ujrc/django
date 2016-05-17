from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseForbidden
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Account

@login_required
def account_detail(request,uuid):
	account=Account.objects.get(uuid=uuid)
	if account.owner !=request.user:
		return httpResponseForbidden()
	variables={
	'account':account,
	}

	return render(request,'accounts/account_detail.html',variables)

class AccountList(ListView):
	model =  Account
	paginate_by=12
	template_name ='accounts/accounts_list.html'
	context_object_name='accounts'

	def get_queryset(self):
		try:
			a=self.request.GET.get('account',)
		except KeyError:
			a=None
		if a:
			accounts_list=Account.objects.filter(
				name__icontains=a,
				owner=self.request.user)
		else:
			accounts_list=Account.objects.filter(owner=self.request.user)
		return accounts_list

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(AccountList,self).dispatch(*args,**kwargs)
	
