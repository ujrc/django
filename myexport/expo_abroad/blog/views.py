from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse,reverse_lazy
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Post


class RestrictToOwnerMixin(LoginRequiredMixin):
	def get_queryset(self):
		return self.model.objects.filter(author=self.request.user)


class CategorySuccessUrlMixin(object):

	def get_success_url(self):
		return reverse('blog:category_list')


class CategoryMixin(object):

	def get_context_data(self,**kwargs):
		context=super(CategoryMixin,self).get_context_data(**kwargs)
		context['categories']=Category.objects.all()
		return context


class CategoryListView(LoginRequiredMixin,ListView):
	model=Category
	template_name='blog/category_list.html'
	

class CategoryDetailView(LoginRequiredMixin,CategoryMixin,DetailView):
	model=Category
	template_name='blog/category_detail.html'



	def get_context_data(self,**kwargs):
		context=super(CategoryDetailView,self).get_context_data(**kwargs)
		context['post_list']=Post.objects.all()
		return context


class CategoryCreateView(CategorySuccessUrlMixin, LoginRequiredMixin,CreateView):
	model= Category
	fields=['title','description']

	def get_context_data(self,**kwargs):
		context = super(CategoryCreateView, self).get_context_data(**kwargs)
		context['name'] = 'Add a new'
		return context


class CategoryUpdateView(LoginRequiredMixin,CategorySuccessUrlMixin,UpdateView):
	model=Category
	fields=['title','description']
	template_name ='blog/category_form.html'

	def get_context_data(self,**kwargs):
		context = super(CategoryUpdateView, self).get_context_data(**kwargs)
		context['name'] = ('Edit '+self.object.title)
		context['post_list']=Post.objects.all()
		return context


class CategoryDeleteView(CategorySuccessUrlMixin,LoginRequiredMixin,DeleteView):
	model=Category
	template_name='object_confirm_delete.html'


class PostListView(LoginRequiredMixin,ListView):
	model =Post
	template_name ='blog/post_list.html'
	context_object_name='post_list'
	
	def get_object(self,queryset=None):
		category=super(PostDetailView,self).get_object(queryset)
		Post.objects.get_or_create(category=self.category)
		return category


class PostDetailView(LoginRequiredMixin,DetailView):
	model=Post
	template_name='blog/post_detail.html'
	

class PostCreateView(RestrictToOwnerMixin,CreateView):
	model= Post
	# template_name ='blog/add_post.html' 
	fields=['author','title','content','status','category']

	def forms_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).forms_valid(form)


class PostUpdateView(RestrictToOwnerMixin,UpdateView):
	model= Post
	template_name ='blog/edit_post.html'
	fields=['title','content','status','category']

	
class PostDeleteView(DeleteView):
	model =Post
	template_name='object_confirm_delete.html'

	def get_success_url(self):
		return reverse("blog:post_detail",kwargs={'slug':self.slug})



