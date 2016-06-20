from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView,DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from .forms import UserForm
from .models import Album,Song


class RestrictToOwnerMixin(LoginRequiredMixin):
	def get_queryset(self):
		return self.model.objects.filter(user=self.request.user)


class HomeView(RestrictToOwnerMixin,ListView):
	model=Album
	template_name='musics/home.html'
	paginate_by = 10

	def get_queryset(self):
			queryset_list=super(HomeView,self).get_queryset()
			query = self.request.GET.get("q")
			if query:
				qs=queryset_list.filter(
					Q(album_title__contains=query)|
					Q(artist__contains=query))
				return qs
			else:
				return queryset_list


class DetailView(DetailView):
	model=Album
	template_name ='musics/detail.html'


class AlbumCreate(CreateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']


class AlbumUpdate(LoginRequiredMixin,UpdateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']


class AlbumDeleteView(LoginRequiredMixin,DeleteView):
	model =Album
	success_url=reverse_lazy('musics:home')
	success_message = " Thing was deleted successfully."

	def delete_album(self, request,* args ,**kwargs):
		messages.success(self.request,self.success_message)
		return super(AlbumDeleteView,self).delete_album(request,*args,**kwargs)


class UserFormView(View):
	form_class=UserForm
	template_name='musics/registration_form.html'

	# Display a blank form
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	# Process form dtat
	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			# Cleaned data( data formated properly)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# retun User objects if credentials are correct
			user=authenticate(username=username, password=password)

			if user  is not None:
				if user.is_active:
					login(self.request,user)
					return redirect('musics:home')
		return render(request,self.template_name,{'form':form})


class SongListView(RestrictToOwnerMixin,ListView):
	model=Song
	template_name='musics/detail.html'

    def get_queryset(self):
        album=get_object_or_404(Album,album_title__iexact=self.args[0])
        return Song.objects.filter(album=album)


class SongDetailView(LoginRequiredMixin,DetailView):
	model= Song
	template_name ='musics/create_song.html'
	context_object_name='song_list'

	def get_queryset(self):
		return self.model.objects.filter(album__user=self.request.user)


class SongCreateView(CreateView):
	model=Song
	fields =['song_title','file_type']

class SongUpdateView(UpdateView):
	model = Song

class SongDeleteView(DeleteView):
	model=Song
	success_url = reverse_lazy('musics:songs')
