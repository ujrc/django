from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect ,HttpResponseForbidden

from accounts import views
from accounts.models import Account
from .forms import ContactForm
from .models import Contact


@login_required
def contact_detail(request,uuid):
	contact=Contact.objects.get(uuid=uuid)

	return render(request,
		'contacts/contact_detail.html',{'contact':contact})

@login_required
def contact_cru(request,uuid=None,account=None):

	if uuid:
		contact=get_object_or_404(Contact,uuid=uuid)
		if contact.owner != request.user:
			return HttpResponseForbidden()
	else:
		contact=Contact(owner=request.user)
		
	if request.POST:
		form = ContactForm(request.POST,instance=contact)
		if form.is_valid():
			# make sure the user owns the account
			account=form.cleaned_data['account']
			if account.owner!=request.user:
				return HttpResponseForbidden()

			# save the data
			contact=form.save(commit=False)
			contact.owner=request.user
			contact.save()
			# return the user to the account detail view
			reverse_url= reverse(
				views.account_detail,args=(account.uuid,))
			return HttpResponseRedirect(reverse_url)
		else:
			# if the form isn't valid, still fetch the account so it can be passed to the template
			account=form.cleaned_data['account']
	else:
		form=ContactForm(instance=contact)
	if request.GET.get('account',''):
		account=Account.objects.get(id=request.GET.get('account',''))
	variables={
	'form':form,
	'contact':contact,
	'account':account
	}
	template_name='contacts/contact_cru.html'
	return render(request,template_name,variables)




