# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models

from django_countries.fields import CountryField
from shortuuidfield import ShortUUIDField


class Client(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    address_one = models.CharField(max_length=120)
    address_two = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    country = country = CountryField(
        blank=True, blank_label='(select country)')
    phone = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'clients'
        ordering = ['name', '-created_on']

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('clients:client_detail', kwargs={'slug': self.uuid})

    def get_update_url(self):
        return reverse('clients:client_edit', args=[self.uuid])

    def get_delete_url(self):
        return reverse('clients:client_delete', args=[self.uuid])
