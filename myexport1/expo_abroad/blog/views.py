from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Post

class RestrictToOwnerMixin(LoginRequiredMixin):
	def get_queryset(self):
		return self.model.objects.filter(user=self.request.user)

class SearchMixin(object):
	def get_queryset(self):
		queryset_list=super(SearchMixin,self).get_queryset()
		query = self.request.GET.get("q")
		if query:
			qs=queryset_list.filter(
				Q(title__contains=query)
				# Q(artist__contains=query)
				)
			return qs
		else:
			return queryset_list

class CategoryListView(ListView):
	model=Category
	template_name='blog/category_list.html'
	context_object_name="category_list"



class CategoryDetailView(DetailView):
	model=Category
	template_name='blog/category_detail.html'

class CategoryCreateView(RestrictToOwnerMixin,CreateView):
	model= Category
	fields=['title']

	def get_success_url(self):
		return reverse('blog:category_list')


class CategoryEditView(RestrictToOwnerMixin,UpdateView):
	model=Category
	template_name='blog/category_edit.html'
	fields=['title']

	def get_success_url(self):
		return reverse('blog:category_list')


class PostDetailView(ListView):
	model=Post
	template_name='blog/post_detail.html'
	context_object_name="post_list"

	def get_object(self,queryset=None):
		category=super(PostDetailView,self).get_object(queryset)
		Post.objects.get_or_create(category=category)
		return category

	def get_success_url(self):
		return reverse("blog:post_detail", kwargs={'slug': self.slug})


class PostCreateView(CreateView):
	model=Post
	fields =['user','title','content','category']
	template_name='blog/post_form.html'

	def get_success_url(self):
		return reverse("blog:post_detail")


	# def get_queryset(self, slug):
	# 	category=get_object_or_404(Category,slug=slug)
	# 	return super(PostListView,self).get_queryset(category=category)
		