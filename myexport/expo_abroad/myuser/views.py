from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile
# Create your views here.

class RestrictToOwnerMixin(LoginRequiredMixin):
	def get_queryset(self):
		return self.model.objects.filter(user=self.request.user)

class UserRegistrationView(CreateView):
	model=User
	form_class=UserRegistrationForm
	template_name='myuser/registration_form.html'
	fields =['username','email','password']

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			# Cleaned data( data formated properly)
			username=form.cleaned_data.get('username')
			password =form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# retun User objects if credentials are correct
			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(self.request,user)
					return redirect('homepage:home')
		return render(request,self.template_name,{'form':form})	



class UserProfileDetailView(LoginRequiredMixin,DetailView):
	model =get_user_model()
	slug_field='username'
	template_name ='myuser/user_detail.html'

	def get_object(self,queryset=None):
		user=super(UserProfileDetailView,self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user
	def get_success_url(self):
		return reverse("myuser:edit_profile", kwargs={'slug': self.request.user})

class UserProfileUpdateView(RestrictToOwnerMixin,UpdateView):
	
	model = UserProfile
	form_class = UserProfileForm
	template_name = "myuser/edit_profile.html"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("myuser:profile", kwargs={"slug": self.request.user})
