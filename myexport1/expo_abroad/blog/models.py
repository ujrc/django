from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
import string
import random
# Create your models here.

def key_gen(y):
	return ''.join(random.choice(string.ascii_letters+string.digits) for x in range(y))

class TimestampModel(models.Model):
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True


class Category(TimestampModel):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=70)

	def __str__(self):
		return '%s'%self.title

	class Meta:
		verbose_name_plural='categories'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = ''.join((slugify(key_gen(10)),slugify(self.title)))
		super(Category, self).save(*args, **kwargs)

	def get_alsolute_url(self):
		return reverse('blog:category_detail',kwargs={'slug':self.slug})	


class Post(TimestampModel):
	user =models.ForeignKey(User)
	title=models.CharField(max_length=100)
	content= models.TextField()
	slug = models.SlugField(max_length=120, unique=True)
	category =models.ForeignKey(Category)


	def __str__(self):
		return '%s'%self.title

	class Meta:
		verbose_name_plural='posts'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
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