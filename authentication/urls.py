from django.urls import path
from authentication.views import userLoginView, UserRegisterView, UserLogoutView, UserLoginView

urlpatterns = [
    # path('login/', userLoginView, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
