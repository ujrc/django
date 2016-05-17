from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden,HttpResponseRedirect 
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .forms import AccountForm
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



@login_required
def account_cru(request):
	if request.Post:
		form=AccountForm(request.Post)
		if form.is_valid():
			account=form.save(commit=Flase)
			account.owner=request.user
			account.save()
			redirect_url = reverse(
				'accounts.views.account_detail',
				args=(account.uuid))
			return HttpResponseRedirect(redirect_url)

	else:
		form=AccountForm()
	variables={
	'form':form,
	}
	template='account_cru.html'
	return render(request,template,variables)


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
	
