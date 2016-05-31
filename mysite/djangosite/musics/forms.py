from django.contrib.auth.models import User
from . models import Song
from django import forms

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','password']


# class SongForm(forms.ModelForm):
# 	class Meta:
# 		model =Song
# 		fields= ['song_title','file_type']