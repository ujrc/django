import stripe

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.forms import NON_FIELD_ERRORS
from django.http import HttpResponseRedirect

from .forms import SubscriberForm
from .models import Subscriber

def subscriber_new(request,template='subscribers/subscriber_new.html'):
	form=SubscriberForm(request.POST)
	if form.is_valid():
		# Unpack form values
		username=form.cleaned_data['username']
		password=form.cleaned_data['password1']
		email=form.cleaned_data['email']
		first_name=form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']

		# Create the User record

		user=User(username=username,email=email,
			first_name=first_name,last_name=last_name)
		user.set_password(password)
		user.save()

		# Create Subscriber Record
		address_one = form.cleaned_data['address_one']
		address_two = form.cleaned_data['address_two']
		city = form.cleaned_data['city']
		state = form.cleaned_data['state']

		subscriber=Subscriber(address_one=address_one,address_two=address_two,
			city=city,state=state,user_sub=user)
		subscriber.save()

		# Process payment (via Stripe)
		fee=settings.SUBSCRIPTION_PRICE
		try:
			stripe_customer=subscriber.charge(request,email,fee)
		except stripe.StripeError as e:
			form.errors[NON_FIELDS_ERRORS]=form.error_clss([e.args[0]])
			# Auto login the user
		auth_u=authenticate(username=username,password=password)
		if auth_u is not None:
			if auth_u.is_active:
				login(request,auth_u)
				return HttpResponseRedirect(reverse('account-list'))
			else:
				return HttpResponseRedirect(reverse(
					'django.contrib.auth.views.login'))
		else:
			return HttpResponseRedirect(reverse('sub_new'))
	else:
		form=SubscriberForm()
	
	return render(request,template,
		{'form':form,
		'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY,})



