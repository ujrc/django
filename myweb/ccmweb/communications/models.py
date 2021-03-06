from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from accounts.models import Account

from shortuuidfield import ShortUUIDField

class Communication(models.Model):
	uuid=ShortUUIDField(unique=True)
	TYPE_LIST=[(1,'Meeting'),(2,'Phone'),(3,'Email')]
	subject=models.CharField(max_length=50)
	notes=models.TextField()
	kind =models.PositiveSmallIntegerField(choices=TYPE_LIST)
	date=models.DateField()
	owner= models.ForeignKey(User,on_delete=models.CASCADE)
	account=models.ForeignKey(Account, on_delete=models.CASCADE)
	Created_on =models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural='communications'

	def __str__(self):
		return '%s'%self.subject

	@models.permalink
	def get_absolute_url(self):
		return 'comm_detail',[self.uuid]

	@models.permalink
	def get_update_url(self):
		return 'comm_update',[self.uuid]

	@models.permalink
	def get_delete_url(self):
		return 'comm_delete',[self.id]