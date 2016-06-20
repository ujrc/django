from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
	content=forms.CharField(widget=forms.Textarea)

	class Meta:
		fields=['name','email','subject','content']
		model=Contact