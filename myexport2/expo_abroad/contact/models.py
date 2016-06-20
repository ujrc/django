from django.db import models
import datetime
from django.core.urlresolvers import reverse
# Create your models here

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=250)
	subject=models.CharField(max_length=200)
	content=models.CharField(max_length=1500)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

	class Meta:
		ordering=['-timestamp']
