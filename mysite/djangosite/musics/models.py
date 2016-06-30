from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    album_logo = models.FileField(max_length=25, blank=True)
    is_favorite = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('musics:albums:album_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return ('%s %s') % (self.album_title, self.artist)

    class Meta:
        verbose_name_plural = 'albums'

    def save(self, *args, **kwargs):
        self.slug = ''.join((slugify(self.album_title), slugify(self.artist)))
        super(Album, self).save(*args, **kwargs)


class Song(models.Model):
    AUDIO_FILE_TYPES = [('wav', 'wav'), ('mp3', 'mp3'), ('ogg', 'ogg')]
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name='albums')
    file_type = models.FileField(max_length=100, choices=AUDIO_FILE_TYPES)
    song_title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=25, blank=True, unique=True)
    is_favorite = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '%s' % (self.song_title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.song_title)
        super(Song, self).save(*args, **kwargs)

    def ge_absolute_url(self):
        return reverse('musics:song_detail:song_detail', kwargs={'slug': self.slug})


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.album_title)
#     qs = Album.objects.filter(slug=slug).order_by("-id")
#     if new_slug is not None:
#         slug = new_slug
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_reciever, sender=Album)
pre_save.connect(pre_save_reciever, sender=Song)
