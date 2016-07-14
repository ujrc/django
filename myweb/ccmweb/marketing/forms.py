from django import forms


class ContactUsForm(forms.Form):
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=False)
	subject=forms.CharField()
	message=forms.CharField(widget=forms.Textarea)
	email=forms.EmailField()
