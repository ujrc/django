from django import forms


class ContatUsForm(forms.Form):
	first_name= forms.CharField()
	last_name= forms.CharField(required=False)
	email= forms.EmailField()
	subject =forms.CharField()
	message= forms.CharField(widget=forms.Textarea)

