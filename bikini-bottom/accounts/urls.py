from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import RegisterView

urlpatterns = [
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('password-change/', PasswordChangeView.as_view(), name='password_change'),
  path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
  path('register', RegisterView, name='register'),
]