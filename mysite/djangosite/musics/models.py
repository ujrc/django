from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
	# user =models.ForeignKey(User)
	artist=models.CharField(max_length=200)
	album_title=models.CharField(max_length=300)
	genre=models.CharField(max_length=80)
	album_logo=models.FileField()

	def get_absolute_url(self):
		return reverse('musics:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return ('%s %s') %(self.album_title,self.artist)
	class Meta:
		verbose_name_plural='albums'


class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.FileField(default='')
	song_title=models.CharField(max_length=120)
	is_favorite=models.BooleanField(default=False)

	def __str__(self):
		return '%s' %(self.song_title)
