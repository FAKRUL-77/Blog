from django.urls import path
from authentication.views import login, UserRegisterView

urlpatterns = [
    path('login/', login),
    path('register/', UserRegisterView.as_view(), name='register'),
]
