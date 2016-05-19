from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden,HttpResponseRedirect

from accounts import views as account_view
from .forms import CommunicationForm
from .models import Communication
@login_required
def comm_detail(request,uuid):
	comm=Communication.objects.get(uuid=uuid)
	if comm.owner !=request.user:
		return HttpResponseForbidden()

	return render(request,'communications.comm_detail.html',{'comm':comm})


@login_required
def comm_new(request):
	if request.POST:
		form=CommunicationForm(request.POST)
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
				account_view.account_detail,args(account.uuid,))
			return HttpResponseRedirect(reverse_url)
	else:
		form=CommunicationForm()
	context_data={
	'form':form,
	}
	template_name= 'communications/comm_cru.html'
	render(request,template_name,context_data)





