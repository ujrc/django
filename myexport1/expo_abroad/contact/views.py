from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext,loader
from django.views.generic import FormView

from .forms import ContactForm
# # Create your views here.

# class Contact(FormView):

#     form_class = ContactForm  # Form class to be used
#     template_name = 'contact/contact.html' # Template to be used
#     success_url = '/'


class ContactFormView(FormView):

	form_class = ContactForm
	template_name = "contact/contact.html"
	success_url = '/'

	def form_valid(self, form):
		if self.request.POST:

			name=form.cleaned_data.get('name')
			email=form.cleaned_data.get('email')
			subject=form.cleaned_data['subject']
			content = form.cleaned_data.get('content')
		# send_mail(
		#     subject=form.cleaned_data.get('subject').strip(),
		#     content=message,
		#     from_email='contact-form@myapp.com',
		#     recipient_list=[from_email,'example@example.com'],
		# )
		return super(ContactFormView, self).form_valid(form)

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			my_form = form.save(commit=False)
# 			my_form.save()
# 			messages.add_message(
# 				request, messages.INFO, 'Your message has been sent. Thank you.'
# 			)
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = ContactForm()
# 	t = loader.get_template('contact/contact.html')
# 	c = RequestContext(request, {'form': form, })
# 	return HttpResponse(t.render(c))
