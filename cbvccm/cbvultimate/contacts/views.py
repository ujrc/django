# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ContactForm
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
    # slug_field='client_id'

 
class ContactCreateView(LoginRequiredMixin,CreateView):
    # form_class=ContactForm
    model=Contact
    template_name='contacts/contact_form.html'
    fields=['first_name','last_name','role','phone','email']
    success_url = '/'

    def form_valid(self, form):
        new_contact= form.save(commit=False)
        new_contact.owner = self.request.user
        this_client = Client.objects.get(pk=self.kwargs['client_id'])
        new_contact.client = this_client
        new_contact.save()
        return super(ContactCreateView, self).form_valid(form)



class ContactUpdateView(UpdateView):
    pass


class ContactDeleteView(DeleteView):
    pass
