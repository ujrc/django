from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse,reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Post

class CategoryListView(LoginRequiredMixin,ListView):
	model=Category
	template_name='blog/category_list.html'
	context_object_name="category_list"

class CategoryDetailView(LoginRequiredMixin,DetailView):
	model=Category
	template_name='blog/category_detail.html'

class CategoryCreateView(CreateView):
	model= Category
	fields=['title','description']

	# success_url='/blog/'
	def get_success_url(self):
		return reverse('blog:category_list')



class CategoryUpdateView(UpdateView):
	model=Category
	fields=['title','description']
	template_name ='blog/category_form.html'
	def get_success_url(self):
		return reverse('blog:category_list')


class CategoryDeleteView(DeleteView):
	model=Category
	# template_name='object_confirm_delete.html'
	
	def get_success_url(self):
		return reverse('category_list')

class PostDetailView(LoginRequiredMixin,ListView):
	model=Post
	template_name='blog/post_detail.html'
	context_object_name="post_list"

	def get_object(self,queryset=None):
		category=super(PostDetailView,self).get_object(queryset)
		Post.objects.get_or_create(category=category)
		return category

	def get_success_url(self):
		return reverse("blog:post_detail", kwargs={'slug': self.slug})


	# def get_queryset(self, slug):
	# 	category=get_object_or_404(Category,slug=slug)
	# 	return super(PostListView,self).get_queryset(category=category)
		