from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import RegisterView, ProfileView, ProfileAddView, ProfileUpdateView

urlpatterns = [
  # path('login/', LoginView.as_view(), name='login'),
  # path('logout/', LogoutView.as_view(), name='logout'),
  # path('password-change/', PasswordChangeView.as_view(), name='password_change'),
  # path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
  path('register', RegisterView, name='register'),
  path('', include('django.contrib.auth.urls')), #for password reset

  # PROFILE PAGE
  path('profile/', ProfileView, name='profile'),
  path('profile/add/', ProfileAddView, name='profile_add'),
  path('profile/update/<int:pk>/', ProfileUpdateView, name='profile_update'),
]
