from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden,HttpResponseRedirect

from accounts import views as account_view
from accounts.models import Account
from .forms import CommunicationForm
from .models import Communication

@login_required
def comm_detail(request,uuid):
	comm=Communication.objects.get(uuid=uuid)
	if comm.owner !=request.user:
		return HttpResponseForbidden()

	return render(request,'communications/comm_detail.html',{'comm':comm})


@login_required
def comm_cru(request,uuid=None,account=None):
	if uuid:
		comm=get_object_or_404(Communication,uuid=uuid)
		if comm.owner!=request.user:
			return HttpResponseForbidden()
	else:
		comm=Communication(owner=request.user)
	if request.POST:
		form=CommunicationForm(request.POST,instance=comm)
		if form.is_valid():
			# make sure the user owns the account
			account=form.cleaned_data['account']
			if account.owner != request.user:
				return HttpResponseForbidden()
			comm=form.save(commit=False)
			comm.owner=request.user
			comm.save()
			# return the user to the account detail view
			reverse_url= reverse(
				account_view.account_detail,args=(account.uuid,))
			return HttpResponseRedirect(reverse_url)
		else:
			# if the form isn't valid, still fetch the account so it can be passed to the template
			account = form.cleaned_data['account']

	else:
		form=CommunicationForm(instance=comm)
	# this is used to fetch the account if it exists as a URL parameter
	if request.GET.get('account', ''):
		account = Account.objects.get(id=request.GET.get('account', ''))
	context_data={
	'form':form,
	'comm':comm,
	'account':account,
	}
	template_name= 'communications/comm_cru.html'
	render(request,template_name,context_data)





