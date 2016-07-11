# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Client


class RestrictToOwnerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToOwnerMixin, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs


class ClientListView(RestrictToOwnerMixin, ListView):
    model = Client
    paginate_by = 10
    context_object_name = 'clients'

    def get_queryset(self):

        try:
            clien = self.request.GET.get('client',)
        except KeyError:
            clien = None
        if clien:
            clients_list = self.model.objects.filter(name__icontains=clien,owner=self.request.user)
        else:
            clients_list = self.model.objects.filter(owner=self.request.user)
        return clients_list


class ClientDetailView(RestrictToOwnerMixin, DetailView):
    model = Client
    slug_field = 'uuid'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'description', 'address_one', 'address_two', 'city',
              'state', 'zip_code', 'country', 'phone']

    def get_context_data(self):
        context = super(ClientCreateView, self).get_context_data()
        context.update({'input': 'Create Client', 'title': 'Add a New Client'})
        return context

    def form_valid(self, form):
        client = form.save(commit=False)
        client.owner = self.request.user
        return super(ClientCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('clients:client_list')


class ClientUpdateView(RestrictToOwnerMixin, UpdateView):
    model = Client
    fields = ['description', 'address_one', 'address_two', 'city',
              'state', 'zip_code', 'country', 'phone']
    slug_field = 'uuid'

    def get_context_data(self):
        context = super(ClientUpdateView, self).get_context_data()
        context.update({'input': 'Update Client', 'title': 'Update Client'})
        return context

    def get_success_url(self):
        return reverse('clients:client_detail', kwargs={'slug': self.object.uuid})


class ClientDeleteView(RestrictToOwnerMixin, DeleteView):
    model = Client
    slug_field = 'uuid'
    template_name = 'object_confirm_delete.html'

    def get_success_url(self):
        return reverse('clients:client_list')
