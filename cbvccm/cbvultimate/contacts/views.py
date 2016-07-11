# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Contact
from clients.models import Client


class RestrictToOwnerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToOwnerMixin, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs


class ContactListView(RestrictToOwnerMixin, ListView):
    queryset = Contact.objects.all()
    model=Contact
    context_object_name='contacts'


class ContactDetailView(RestrictToOwnerMixin, DetailView):
    model = Contact
    context_object_name = 'contacts'

 
class ContactCreateView(CreateView):
    model=Contact
    slug_field='uuid'
    fields=['first_name','last_name','role','phone','email']


class ContactUpdateView(UpdateView):
    pass


class ContactDeleteView(DeleteView):
    pass
