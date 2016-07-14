# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


from .forms import ContactUsForm


class HomePage(TemplateView):
	""" Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.    """
	template_name='marketing/home.html'
class AboutUsView(TemplateView):
	template_name='marketing/about.html'

class ContactUsView(FormView):
	form_class=ContactUsForm
	template_name='marketing/contactus.html'

	def form_valid(self,form):
		from_email=form.cleaned_data['email']
		message='{first_name}/{email} :'.format(form.cleaned_data.get('first_name'),
			email=form.cleaned_data['email'])
		message+="\n\n{0}".format(form.cleaned_data['message'])
		send_mail(
			subject=form.cleaned_data['subject'].strip(),
			message=message,
			from_email=email,
			recipient_list=[settings.LIST_OF_RECIPIENTS])
		return super(ContactUsView,self).form_valid(form)


		