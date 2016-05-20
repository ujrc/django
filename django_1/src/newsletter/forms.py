from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields = ['full_name','email'] # we can also use exclude fields (not good)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base,provider =email.split('@')
		domain,extension=provider.split('.')
		if not domain == 'USC'.lower():
			raise(forms.ValidationError('Please make sure you use your USC email.'))
		if extension !='edu':
		# if not "edu" in email:
			raise forms.ValidationError("Please use a valid .edu email address")

		return email

	def clean_full_name(self):
		full_name=self.cleaned_data.get('full_name')
		if len(full_name)<5:
			raise forms.ValidationError("Too short name. Please enter a valid name")
		return full_name