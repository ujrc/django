from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput())
	 
	class Meta:
		model = User
		fields =['username','email','password']

class UserProfileForm(forms.ModelForm):
	class Meta:

		model=UserProfile
		fields=['biography','profession','gender','birthdate',
				'avatar' ]
