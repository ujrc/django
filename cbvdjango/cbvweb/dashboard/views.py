# Create your views here.
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin,ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView, DeleteView, UpdateView,ModelFormMixin)
from django.views.generic.list import ListView
from django.shortcuts import render
from django.utils.decorators import method_decorator

from.forms import BookForm
from .models import Book

# FBV

# def book_detail(request,slug):
# 	book=Book.objects.get(slug=slug)
# 	return render()

class MultipleObjectMixin(object):
	def get_object(self,queryset=None,*args,**kwargs):
		slug=self.kwargs.get('slug')
		if slug:
			try:
				obj=self.model.objects.get(slug=slug)				
			except self.model.MultipleObjectsReturned:
				obj=self.get_queryset().first()
			except:
				raise Http404
			return obj
		raise Http404

class BookCreateView(SuccessMessageMixin,CreateView):
	model=Book
	fields =['title','description']
	template_name='dashboard/form.html'
	success_message ='%(title)s has been created at %(created_at)s'

	def form_valid(self,form):
		print (form.instance)
		# success_url='/'# for static urls
		form .instance.added_by=self.request.user
		# form.instance.last_edit_by =self.request.user
		form_valid=super(BookCreateView,self).form_valid(form)
		# messages.success(self.request,'Book Created')
		return form_valid

	# for dynamic url
	def get_success_url(self):
		# messages.success(self.request,'Book Created')
		return reverse('book_list')

	def get_success_message(self,cleaned_data):
		return self.success_message %dict(
			cleaned_data,
			created_at= self.object.timestamp,)

class BookDeleteView(DeleteView):
	model=Book

	def get_success_url(self):
			return reverse('book_list')


class BookUpdateView(MultipleObjectMixin,UpdateView):
	model=Book
	#fields=['title','description']
	form_class =BookForm
	template_name='dashboard/form.html'


class BookDetail(SuccessMessageMixin,ModelFormMixin,MultipleObjectMixin,DetailView):
	model=Book
	form_class =BookForm
	success_message ="%(title)s has been updated"

	def get_context_data(self,*args,**kwargs):
		context=super(BookDetail,self).get_context_data(*args,**kwargs)
		context['form']=self.get_form()
		context['btn_title']='Update Book'
		return context

	def post(self,request,*args,**kwargs):
		if request.user.is_authenticated():
			self.object=self.get_object()
			form=self.get_form()
			if form.is_valid():
				return self.form_valid(form)
			else:
				return self.form_invalid(form)

	# def dispatch(self,request,*args,**kwargs):
	# 	messages.success(self.request,'Book Viewed')
	# 	return super(BookDetail,self).dispatch(request,*args,**kwargs)

	
class BookListView(ListView):
	model=Book

	def get_queryset(self,*args,**kwargs):
		qs=super(BookListView,self).get_queryset(*args,**kwargs).order_by('-timestamp')
		# print(qs)
		# print(qs.first())
		return qs
	# def get_context_data(self,*args,**kwargs):
	# 	context=super(BookDetail,self).get_context_data(*args,**kwargs)
	# 	print (context)
	# 	return context

class LoginRequiredMixin(object):
	## Method 1
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)
	## method 2
	# @classmethod
	# def as_view(cls,**kwargs):
	# 	view=super(LoginRequiredMixin,cls).as_view(**kwargs)
	# 	return login_required(view)

class DashboardTemplateView(LoginRequiredMixin,TemplateView):
	template_name='about.html'


	def get_context_data(self,*args,**kwargs):
		context=super(DashboardTemplateView,self).get_context_data(*args,**kwargs)
		context['title']='About us Page' # This method used to change context of data to be rendered
		return context

# Using class based View
class MyView(LoginRequiredMixin,TemplateResponseMixin,ContextMixin,View):

	
	def get(self,request,*args,**kwargs):
		context=self.get_context_data(**kwargs)
		context['title']='Some other title'
		return self.render_to_response(context)

	# @method_decorator(login_required)
	# def dispatch(self,request,*args,**kwargs):
	# 	return super(MyView,self).dispatch(request,*args,**kwargs)