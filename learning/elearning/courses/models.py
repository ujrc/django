# Create your models here.
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

from .fields import OrderField


#BaseContent
class BaseItemContent(models.Model):
	owner = models.ForeignKey(User,related_name='%(class)s_related')
	name =models.CharField(max_length=220)
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

	def __str__(self):
		return self.name


class Text(BaseItemContent):
	content = models.TextField()

class File(BaseItemContent):
	file =models.FileField(upload_to='files')

class Image(BaseItemContent):
	image =models.ImageField(upload_to='imgaes')

class Video(BaseItemContent):
	url =models.URLField()
	video =models.FileField(upload_to='videos', blank=True,null=True)


class Subject(models.Model):
	name =models.CharField(max_length=220)
	slug=models.SlugField(max_length=220,unique=True)

	class Meta:
		verbose_name_plural='subjects'
		ordering=['name']

	def __str__(self):
		return self.name
class Course(models.Model):
	owner =models.ForeignKey(User,related_name='course_created')# courses_created
	subject=models.ForeignKey(Subject,related_name='course', on_delete=models.CASCADE)# courses
	name = models.CharField(max_length=220) # title
	slug = models.SlugField(max_length=220,unique=True)
	overview =models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['-created_on']#created
		verbose_name_plural='courses'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('course_list')

class Module(models.Model):
	course = models.ForeignKey(Course, related_name='modules')
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True,null=True)
	order =OrderField(blank=True, order_fields=['course'])

	def __str__(self):
		return '{}.{}'.format(self.order,self.name)

class Contents(models.Model):
	module =models.ForeignKey(Module,related_name='content')#contents
	content_type=models.ForeignKey(ContentType, limit_choices_to={'model__in':['text',
		'file','image','video']})
	object_id= models.PositiveIntegerField()
	item =GenericForeignKey('content_type','object_id')
	order = OrderField(blank=True, order_fields=['module'])


	class Meta:
		ordering =['order']

