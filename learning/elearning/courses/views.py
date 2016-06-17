# Create your views here.
from braces.views import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .forms import ModuleFormSet
from .models import Course

class OwnerMixin(object):

	def get_queryset(self):
		queryset=super(OwnerMixin,self).get_queryset()
		return queryset.filter(owner=self.request.user)


class OwenerEditMixin(object):

	def form_valid(self,form):
		form.instance.owner=self.request.user
		return super(OwenerEditMixin,self).form_valid(form)

class CourseOwnerMixin(OwnerMixin,LoginRequiredMixin):
	model=Course

class CourseOwnerEditMixin(CourseOwnerMixin,OwenerEditMixin):
	fields=['subject','name','slug','overview']
	template_name = 'courses/course_form.html'

	def get_success_url(self):
		return reverse('course_list')


class CourseListView(CourseOwnerMixin,ListView):
	template_name ='courses/course_list.html'


class CourseCreateView(PermissionRequiredMixin,CourseOwnerEditMixin, CreateView):	
	permission_required='courses.add_course'


class CourseUpdateView(PermissionRequiredMixin,CourseOwnerEditMixin, UpdateView):
	template_name = 'courses/course_form.html'
	permission_required='courses.change_course'


class CourseDeleteView(PermissionRequiredMixin,CourseOwnerMixin, DeleteView):
	template_name = 'courses/delete.html'
	success_url = reverse_lazy('course_list')
	permission_required='courses.delete_course'


class CourseModuleUpdateView(TemplateResponseMixin,View):
	template_name = 'courses/formset.html'
	course=None

	def get_formset(self,data=None):
		return ModuleFormSet(instance=self.course,data=data)

	def dispatch(self,request,pk):
		self.course = get_object_or_404(
			Course,id=pk,
			owner=request.user)
		return super(CourseModuleUpdateView,self).dispatch(request,pk)

	def get(self,request,*args,**kwargs):
		formset=self.get_formset()
		return self.render_to_response({'course':self.course,
			'formset':formset})

	def post(self,request,*args,**kwargs):
		formset=self.get_formset(data=request.POST)
		if formset.is_valid():
			formset.save()
			return redirect('course_list')
		return self.render_to_response({'course':self.course,
			'formset':formset})



