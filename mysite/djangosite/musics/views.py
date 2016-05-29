from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from .models import Album,Song
from .forms import UserForm 

from django.views.generic.base import TemplateView
from django.db.models import Q
class HomePage(TemplateView):
	""" Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.    """
	template_name='marketing/homepage.html'

class HomeView(generic.ListView):
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


class DetailView(generic.DetailView):
	model=Album
	template_name ='musics/detail.html'

	
class AlbumCreate(CreateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(AlbumCreate,self).dispatch(*args,**kwargs)


class AlbumUpdate(UpdateView):
	model =Album
	fields=['artist','album_title','genre','album_logo']

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(AlbumUpdate,self).dispatch(*args,**kwargs)

		
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
			usr=form.save(commit=False)

			# Cleaned data( data formated properly)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			usr.set_password(password)
			usr.save()
			# retun User objects if credentials are correct
			usr=authenticate(username=username, password=password)

			if usr  is not None:
				if usr.is_active:
					login(request,usr)
					return redirect('musics:home')
		return render(request,self.template_name,{'form':form})




