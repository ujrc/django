# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from clients.models import Client

from shortuuidfield.fields import ShortUUIDField


class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=35)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='contacts')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'contacts'
        ordering = ['client', 'modified_on']

    @property
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('contacts:contact_detail', kwargs={'pk': self.client.id})

    def get_update_url(self):
        return reverse('contacts:contact_edit', args=[self.id])

    def get_delete_url(self):
        return reverse('contacts:contact_delete', args=[self.id])
