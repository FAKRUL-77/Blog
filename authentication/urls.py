from django.urls import path
from authentication.views import userLoginView, UserRegisterView

urlpatterns = [
    # path('login/', userLoginView.as_view(), name='login'),
    path('login/', userLoginView, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
