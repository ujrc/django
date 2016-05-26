from django.db import models

# Create your models here.

class Album(models.Model):
	artist=models.CharField(max_length=200)
	album_title=models.CharField(max_length=300)
	genre=models.CharField(max_length=80)
	album_logo=models.CharField(max_length=1000)

	def __str__(self):
		return ('%s %s') %(self.album_title,self.artist)
	class Meta:
		verbose_name_plural='albums'


class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=120)

	def __str__(self):
		return '%s' %(self.song_title)
