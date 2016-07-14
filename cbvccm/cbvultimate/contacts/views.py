# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404
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


class GetObjectMixin(object):

    def get_object(self, queryset=None):
        obj = super(GetObjectMixin, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        client = Client.objects.get(pk=obj.client.id)
        return obj


class ContactListView(GetObjectMixin, RestrictToOwnerMixin, ListView):
    model = Contact
    context_object_name = 'contacts'

# class ContactDetailView(RestrictToOwnerMixin, DetailView):
#     model = Contact
#     context_object_name = 'contacts'


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'role', 'phone', 'email']

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context.update({'input': 'Create Contact',
                        'title': 'Add a New Contact'})
        return context

    def form_valid(self, form):
        new_contact = form.save(commit=False)
        new_contact.owner = self.request.user
        _client = Client.objects.get(pk=self.kwargs['client_id'])
        new_contact.client = _client
        new_contact.save()
        return super(ContactCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('clients:client_list')


class ContactUpdateView(GetObjectMixin, RestrictToOwnerMixin, UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'role', 'phone', 'email']
    slug_field = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(ContactUpdateView, self).get_context_data(**kwargs)
        context.update({'input': 'Update Contact', 'title': 'Update Contact'})
        return context

    def get_success_url(self):
        return reverse('contacts:contact_list')


class ContactDeleteView(GetObjectMixin, RestrictToOwnerMixin, DeleteView):
    model = Contact
    template_name = 'object_confirm_delete.html'

    def get_success_url(self):
        return reverse('clients:client_list')
