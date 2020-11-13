from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import CreateView


from authentication.models import MyUser
from .forms import RegistrationForm, UserLoginForm


# LOGIN VIEW ENDPOINT
def userLoginView(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html')
        else:
            form = UserLoginForm
            context = {
                'form':form,
            }
            return render(request, 'login.html', context)
    else:
        return redirect('/')


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
