from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput())
	 
	class Meta:
		model = User
		fields =['username','email','password']

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=40, required=False)
	last_name  = forms.CharField(max_length=40, required=False)


	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model=UserProfile
		widget = {'birthdate': forms.DateInput(attrs={'id': 'id_birthdate'})}
		fields=['first_name','last_name','biography','profession','gender',
				'avatar','birthdate' ]
	def save(self, *args, **kwargs):
		instance = super(UserProfileForm, self).save(*args, **kwargs)
		user = instance.user
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return instance

