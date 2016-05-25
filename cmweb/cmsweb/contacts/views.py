from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,Http404 ,HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from accounts import views

from accounts.models import Account
from .forms import ContactForm
from .models import Contact


@login_required
def contact_detail(request,uuid):
	contact=Contact.objects.get(uuid=uuid)
	if comm.owner !=request.user:
		return HttpResponseForbidden()
	template='contacts/contact_detail.html'
	return render(request,template,{'contact':contact})

@login_required
def contact_create(request,uuid=None,account=None):
	if uuid:
		contact = get_object_or_404(Contact,uuid=uuid)
		if contact.owner != request.user:
			return HttpResponseForbidden()
	else:
		contact = Contact(owner=request.user)

	if request.POST:
		form=ContactForm(request.POST,instance=contact)
		if form.is_valid():
			# make sure the user owns the account
			
			account=form.cleaned_data['account']
			if account.owner != request.user:
				return HttpResponseForbidden()
			# contact = form.save(commit=False)
			# contact.owner = request.user
			# contact.save()
			form.save()
			if request.is_ajax():
				return render(request,
							'contacts/contact_item_view.html',
							{'contact':contact,'account':account}
			  )
			else:
				reverse_url = reverse('accounts.views.account_detail',
					args=(account.uuid,))
				return HttpResponseRedirect(reverse_url)
		else:
			account = form.cleaned_data['account']
	else:
		form = ContactForm(instance=contact)

	if request.GET.get('account', ''):
		account = Account.objects.get(id=request.GET.get('account', ''))

	variables = {'form': form,
				'contact': contact,
				'account': account
				}

	if request.is_ajax():
		template = 'contacts/contact_item_form.html'
	else:
		template = 'contacts/contact_cru.html'

	return render(request, template, variables)


class ContactMixin(object):
	model=Contact

	def get_context_data(self,**kwargs):
		kwargs.update({'object_name':'Contact'})
		return kwargs

	@method_decorator
	def dispatch(self,*args,**kwargs):
		return super(ContactMixin,self).dispatch(*args,**kwargs)


class ContactDelete(ContactMixin,DeleteView):
	template_name= 'object_confirm_delete.html'

	def get_object(self,queryset=None):
		obj=super(ContactDelete,self).get_object()
		if not obj.owner ==self.request.user:
			raise Http404
		account =Account.objects.get(id=obj.account.id)
		self.account=account 
		return obj

	def get_success_url(self):
		return reverse(views.account_detail,args=(self.account.uuid))