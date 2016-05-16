from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Subscriber(models.Model):
	user_sub=models.ForeignKey(User)
	address_one =models.CharField(max_length=100)
	address_two =models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=80)
	state = models.CharField(max_length=2)
	stripe_id=models.CharField(max_length=30,blank=True)

	class Meta:
		verbose_name_plural='subscribers'

	def __str__(self):
		return "%s's Subscription Info" % self.user_sub