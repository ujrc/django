from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from .models import Album,Song
from .forms import UserForm 

from django.views.generic.base import TemplateView
from django.db.models import Q

class HomeView(ListView):
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


# class LoginRequiredMixin(object):
# 	"""Ensures that user must be authenticated in order to access view."""

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

		
class RestrictToOwnerMixin(LoginRequiredMixin):
	def get_queryset(self):

		return self.model.objects.filter(user=self.request.user)


class DetailView(DetailView):
	model=Album
	template_name ='musics/detail.html'

	
class AlbumCreate(CreateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']
	

class AlbumUpdate(UpdateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']

	def get_queryset(self):
		qs = super(AlbumUpdate, self).get_queryset()
		# replace this with whatever makes sense for your application
		return qs.filter(user=self.request.user)

		
class AlbumDelete(DeleteView):
	model =Album
	success_url=reverse_lazy('musics:home')


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


class SongDetailView(LoginRequiredMixin,DetailView):
	model= Song
	template_name ='musics/song_list.html'
	context_object_name='song_list'

	def get_context_data(self,**kwargs):
		context =super(Song,self).get_context_data(**kwargs)
		context['slug'] =self.kwargs['slug']
		return context

	def get_queryset(self):
		album =Album.objects.get(user=self.request.user)
		if album.user_id:
			return Song.objects.filter(album=album)
