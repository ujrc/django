# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse 
from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from . forms import UserForm


class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/registration_form.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form dtat
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Cleaned data( data formated properly)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # retun User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(self.request, user)
                    return redirect('musics:albums:home')
        return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('musics:albums:home')
