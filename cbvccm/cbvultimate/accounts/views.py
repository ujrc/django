# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import UserRegistrationForm
from .models import UserProfile


class RestrictToUserMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToUserMixin, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/accounts_form.html'

    def form_valid(self, form):
        if form.is_valid:
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user = authenticate(username=username, password=password)
        return super(UserRegistrationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:login')


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'accounts/userprofile_detail.html'

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


class UserProfileEditView(UpdateView):
    model = UserProfile
    fields = ['biography', 'birthday', 'gender', 'avatar', 'profession']

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.request.user})
