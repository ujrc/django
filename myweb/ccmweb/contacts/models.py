from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

from accounts.models import Account

from shortuuidfield  import ShortUUIDField 

class Contact(models.Model):
	uuid=ShortUUIDField(unique=True)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	role = models.CharField(max_length=60)
	phone=models.CharField(max_length=16)
	email=models.EmailField()
	account=models.ForeignKey(Account,on_delete=models.CASCADE)
	owner= models.ForeignKey(User,on_delete=models.CASCADE)
	created_on=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='contacts'

	@property
	def full_name(self):
		return u'%s %s' % (self.first_name, self.last_name)

	def __str__(self):
		return u'%s' % self.full_name

	@models.permalink
	def get_absolute_url(self):
		return 'contact_detail',[self.uuid]


	@models.permalink
	def get_update_url(self):
		return 'contact_update', [self.uuid]

	@models.permalink
	def get_delete_url(self):
		return 'contact_delete', [self.id]


	
	



