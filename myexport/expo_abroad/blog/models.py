# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

import datetime
import random
import string

def key_gen(y):
	return ''.join(random.choice(string.ascii_letters+string.digits) for x in range(y))


class PostManager(models.Manager):
	def published(self):
		return self.get_query_set().filter(status='p')


class TimestampModel(models.Model):
	created= models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True


class Category(TimestampModel):
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField('description')
	slug = models.SlugField(max_length=70)

	def __str__(self):
		return '%s'%self.title

	class Meta:
		verbose_name_plural='categories'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = '-'.join((slugify(key_gen(10)),slugify(self.title)))
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:category_detail',kwargs={'slug':self.slug})	


STATUS_CHOICES=[
('d','draft'),
('p','Published')]


class Post(TimestampModel):
	author =models.ForeignKey(User, related_name='author')
	title=models.CharField(max_length=100)
	content= models.TextField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='d')
	published =models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(max_length=120, unique=True)
	category =models.ForeignKey(Category, related_name='posts',on_delete=models.CASCADE)


	def publish(self):
		published=timezone.now()
		return published
		
	def __str__(self):
		return '%s'%self.title

	class Meta:
		verbose_name_plural='posts'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = ''.join((slugify(self.author),slugify(key_gen(10)),slugify(self.title)))#,slugify(self.title),(slugify(key_gen(6)))
		super(Post, self).save(*args, **kwargs)
		

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'slug':self.slug})


class Comment(models.Model):
	name = models.CharField(max_length=42)
	email = models.EmailField(max_length=75)
	website = models.URLField(max_length=200, null=True, blank=True)
	text = models.TextField()
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return '%s'%self.name