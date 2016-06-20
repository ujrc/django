from datetime import date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save



# Create your models here.


# Create your models here.
# class TimestampModel(models.Model):
# 	timestamp=models.DateTimeField(auto_now_add=True)
# 	modified=models.DateTimeField(auto_now=True)

# 	class Meta:
# 		abstract=True
class UserProfile(models.Model):
	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female')
    ]
	user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
	birthdate =models.DateField(blank=True,null=True)
	biography =models.TextField(blank=True,null=True)
	gender =models.CharField(max_length=1, choices=GENDER_CHOICES)
	avatar =models.ImageField(upload_to='uploads/avatars', default='', blank=True)
	profession=models.CharField(max_length=100, blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)

	@property
	def age(self):
		now=date.today()
		delta=now.year - self.birthdate.year - int((now.month, now.day) < (self.birthdate.month, self.birthdate.day))
		return delta

	def __str__(self):
		return '{}'.format(self.user)


	def get_absolute_url(self):
		return reverse('myuser:profile',kwargs={'slug': self.user.username})

	class Meta:
		verbose_name_plural='myusers'	

class Address(models.Model):
	owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
	street_adress1=models.CharField(max_length=120,null=True,blank=True)
	adress2=models.CharField(max_length=120,null=True,blank=True)
	city=models.CharField(max_length=80,blank=True,null=True)
	state =models.CharField(max_length=30,blank=True,null=True)
	counrty=models.CharField(max_length=40,blank=True,null=True)

	def __str__(self):
		return "%s" %self.owner

	class Meta:
		verbose_name_plural='adrresses'

def create_profile(sender,instance,created,**kwargs):
	if created:
		profile,created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile,sender=User)