# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from . models import Communication
from clients.models import Client


class RestrictToUserMixin(LoginRequiredMixin):

    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class GetObjectMixin(object):

    def get_object(self, queryset=None):
        comm = super(GetObjectMixin, self).get_object()
        if not comm.owner == self.request.user:
            raise Http404
        client = Client.objects.get(pk=comm.client.id)
        return comm


class CommListView(GetObjectMixin, RestrictToUserMixin, ListView):
    model = Communication
    context_object_name = 'communications'


class CommDetailView(GetObjectMixin, RestrictToUserMixin, DetailView):
    pass


class CommCreateView(GetObjectMixin, RestrictToUserMixin, CreateView):
    model = Communication
    fields = ['subject', 'notes', 'kind', 'date']

    def form_valid(self, form):
        commu = form.save(commit=False)
        commu.owner = self.request.user
        _client = Client.objects.get(pk=self.kwargs['client_id'])
        commu.client = _client
        commu.save()
        return super(CommCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('clients:client_list')


class CommUpdateView(GetObjectMixin, RestrictToUserMixin, UpdateView):
    model = Communication
    fields = ['subject', 'notes', 'kind', 'date']

    def get_success_url(self):
        return reverse('communications:comm_list')


class CommDeleteView(GetObjectMixin, RestrictToUserMixin, DeleteView):
    model = Communication
    template_name = 'object_confirm_delete.html'

    def get_success_url(self):
        return reverse('communications:comm_list')
