from django.contrib.auth import authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, redirect

# LOGIN VIEW ENDPOINT
from django.views.generic import CreateView

from authentication.models import MyUser
from .forms import RegistrationForm


def login(request):
    return render(request, 'login.html')


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