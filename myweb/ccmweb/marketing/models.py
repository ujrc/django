from django.db import models

# Create your models here.

class ContactUs(models.Model):
	name =models.CharField(max_length=60)
	email =models.CharField(max_length=40)
	subject=models.CharField(max_length=80)
	message=models.TextField()


	def __str__(self):
		return self.name