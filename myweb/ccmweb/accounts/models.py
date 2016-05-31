from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.core.urlresolvers import reverse
class Account(models.Model):
	uuid=ShortUUIDField(unique=True)
	name=models.CharField(max_length=100)
	desc=models.TextField(blank=True)
	address_one = models.CharField(max_length=120)
	address_two = models.CharField(max_length=120,blank=True)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=2)
	phone = models.CharField(max_length=16)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	created_on=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='accounts'


	def __str__(self):
		return "%s" %self.name

	def get_absolute_url(self):
		return reverse('account_detail',{uuid=self.uuid})

	@models.permalink
	def get_update_url(self):
		return 'account_update',[self.uuid]

	@models.permalink
	def get_delete_url(self):
		return 'account_delete',[self.uuid]


