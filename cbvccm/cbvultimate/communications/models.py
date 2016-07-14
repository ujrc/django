# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from shortuuidfield.fields import ShortUUIDField

from clients.models import Client


class Communication(models.Model):
    uuid_com = ShortUUIDField(unique=True)
    TYPE_CHOICES = [(1, 'Meeting'),
                    (2, 'Email'),
                    (3, 'Phone')]
    subject = models.CharField(max_length=60)
    notes = models.TextField()
    kind = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='communications')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'communications'
        ordering = ['-date', 'client']
        unique_together = ['date', 'owner']

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('communications:comm_detail', kwargs={'slug':self.uuid_com})

    def get_update_url(self):
        return reverse('communications:comm_edit', args=[self.uuid_com])

    def get_delete_url(self):
        return reverse('communications:comm_delete', args=[self.id])
