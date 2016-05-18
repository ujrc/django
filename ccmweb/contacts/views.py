from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect ,HttpResponseForbidden

from .forms import ContactForm
from .models import Contact


@login_required
def contact_cru(request):
	if request.POST:
		form=ContactForm(request.POST)
		if form.is_valid():
			# make sure the user owns the account
			account=form.cleaned_data['account']
			if account.owner= !request.user:
				return HttpResponseRedirect()

			# save the data
			contact=form.save(commit=False)
			contact.owner=request.user
			contact.save()
			# return the user to the account detail view
			reverse_url= reverse(
				'account/account_detail.html',args=(account.uuid,))
			return HttpResponseRedirect(reverse_url)
	else:
		form=ContactForm()
		variables={
		'form':form,
		}
		template_name='contacts/contact_cru.html'
		return HttpResponseRedirect(request,template_name,variables)




@login_required
def contact_detail(request,uuid):
	contact=Contact.objects.get(uuid=uuid)

	return render(request,
		'contacts/contact_detail.html',{'contact':contact})


