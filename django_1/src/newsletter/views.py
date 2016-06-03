from django.shortcuts import render
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignUpForm, ContactForm
def home(request):
	title="Welcome"
	# if request.user.is_authenticated():
	# 	title="My title %s" %(request.user) 

	#Add form
	# if request.POST:
	# 	print(request.POST)
	form =SignUpForm(request.POST or None)
	context={
	'title':title,
	'form':form,
	}
	if form.is_valid():
		# form.save()
		# print(request.POST['email']) # This is not good  don't save data through request

		instance=form.save(commit=False)
		full_name=form.cleaned_data.get('full_name')
		if not full_name:
			full_name="My name"
		instance.full_name=full_name
		instance.save()
		# print(instance.email)
		# print(instance.full_name)
		context={
		'title':'Thank you for joining us',
		}
	if request.user.is_authenticated and request.user.is_staff:
		context={
		'queryset':[123,456]
		}
	return render(request,'newsletter/home.html',context)

def contact(request):
	title="Contact Us"
	title_align_center=True
	form=ContactForm(request.POST or None)
	if form.is_valid():
		from_email=form.cleaned_data.get('email')
		from_message=form.cleaned_data['message']
		from_full_name=form.cleaned_data['full_name']
		subject='Site Contact Form'
		from_email=settings.EMAIL_HOST_USER
		to_email =[from_email,'otheremail@gmail.com']
		contact_message ="%s:%s via %s" %(
			from_full_name,
			from_message,
			from_email)

		send_mail(subject,
			contact_message,
			from_email,to_email,fail_silently=False)
		# print (email,full_name,message)
		# print(form.cleaned_data)
		# for key in form.cleaned_data:
		# 	# print (key)
		# 	print(form.cleaned_data[key])
		# 	print(form.cleaned_data.get(key))
	context={
	'form':form,
	'title':title,
	'title_align_center':title_align_center,
	}
	template='newsletter/forms.html'

	return render(request,template,context)