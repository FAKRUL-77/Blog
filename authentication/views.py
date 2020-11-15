from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import CreateView


from authentication.models import MyUser
from .forms import RegistrationForm, UserLoginForm


# REGISTRATION VIEW ENDPOINT
class UserRegisterView(CreateView):
    model = MyUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        return redirect('/')


# LOGOUT VIEW ENDPOINT
class UserLogoutView(LogoutView):
    template_name = 'base'
    next_page = '/'


# LOGOUT VIEW ENDPOINT
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
