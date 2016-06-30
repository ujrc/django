from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Album, Song


class SearchMixin(object):

    def get_queryset(self):
        queryset_list = super(SearchMixin, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = queryset_list.filter(
                Q(album_title__contains=query) |
                Q(artist__contains=query))
            return qs
        else:
            return queryset_list


# class RestrictToOwnerMixin(LoginRequiredMixin):
# 	def get_queryset(self):
# 		return self.model.objects.filter(user=self.request.user)


class AlbumListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Album
    template_name = 'musics/home.html'
    context_object_name = 'albums'
    paginate_by = 10

    def get_queryset(self):
        queryset_list = super(AlbumListView, self).get_queryset()
        queryset_list=Album.objects.filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            qs = queryset_list.filter(
                Q(album_title__contains=query) |
                Q(artist__contains=query))
            return qs
        else:
            return queryset_list
    


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'musics/album_detail.html'

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=Album.objects.all())
    #     return super(AlbumDetailView, self).get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(AlbumDetailView, self).get_context_data(**kwargs)
    #     context['album'] = self.object
    #     context.update({'songs': Song.objects.all()})
    #     return context


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def form_valid(self, form):
        album = form.save(commit=False)
        album.user = self.request.user
        album.save()  # This is redundant, see comments.
        return super(AlbumCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('musics:albums:home')


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album

    def get_success_url(self):
        return reverse('musics:albums:home')
    # success_message = " Thing was deleted successfully."
    # template_name='object_confir'

    # def delete_album(self, request,* args ,**kwargs):
    # 	messages.success(self.request,self.success_message)
    # 	return super(AlbumDeleteView,self).delete_album(request,*args,**kwargs)


class SongListView(LoginRequiredMixin, ListView):
    queryset = Song.objects.all().order_by('-updated')[:5]
    context_object_name = 'songs'
    paginate_by = 10
    # template_name = 'musics/song_list.html'


class SongDetailView(LoginRequiredMixin, DetailView):
    model = Song
    template_name = 'musics/create_song.html'
    # context_object_name = 'songs'

    def get_queryset(self):
        album=get_object_or_404(Album)
        return self.model.objects.filter(album__user=self.request.user)


class SongCreateView(LoginRequiredMixin,CreateView):
    model = Song
    fields = ['song_title', 'file_type']

    def get_success_url(self):
        return reverse('musics:songs:song_list')

    def form_valid(self, form):
        song = form.save(commit=False)
        song.album__user = self.request.user
        song.save()  # This is redundant, see comments.
        return super(SongCreateView, self).form_valid(form)


class SongUpdateView(UpdateView):
    model = Song
    fields = ['song_title', 'file_type']


class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('musics:songs:song_list')
