from django.urls import path
from tourism import views

urlpatterns = [
  # PAGE
  path('', views.HomeView, name='home'),
  path('profile/', views.ProfileView, name='profile'),
  path('profile/add/', views.ProfileAddView, name='profile_add'),
  path('profile/update/<int:pk>/', views.ProfileUpdateView, name='profile_update'),

  # API
  path('geo-facility/', views.FacilityGeoView, name='geo_facility'),
  path('geo-infrastructure/', views.LineInfrastructureGeoView, name='geo_infrastructure'),
  path('geo-district/', views.DistrictGeoView, name='geo_district'),
]