from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import ContatUsForm
# Create your views here.


class MainPage(TemplateView):
	template_name = 'main/homepage.html'


class AboutView(TemplateView):
	template_name = 'main/about.html'

class ContactUsView(FormView):
	form_class=ContatUsForm
	template_name='main/contactus_form.html'
	def form_valid(self,form):
		from_email=form.cleaned_data['email']
		message ="{first_name}/{email} :".format(
			first_name=form.cleaned_data['first_name'],
			email=form.cleaned_data['email'])
		message+="\n\n{0}".format(form.cleaned_data.get('message'))
		send_mail(
			subject=form.cleaned_data['subject'].strip(),
			message=message,
			from_email=from_email,
			recipient_list=[settings.LIST_OF_RECIPIENTS],
		)
		return super(ContactUsView, self).form_valid(form)


class PrivacyView(TemplateView):
	template_name='main/privacy.html'

class CopyRightView(TemplateView):
	template_name='main/copyright.html'


class TermsView(TemplateView):
	template_name='main/terms.html'
