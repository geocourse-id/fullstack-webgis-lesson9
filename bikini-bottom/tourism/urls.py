from django.urls import path
from tourism import views

urlpatterns = [
  # HOME PAGE
  path('', views.HomeView, name='home'),

  # BOOKING PAGE
  path('booking/', views.BookingView, name='booking'),
  path('booking/add/', views.BookingAddView, name='booking_add'),

  # FACILITY PAGE
  path('facility/', views.FacilityView, name='facility'),
  path('facility/propose/', views.FacilityProposeView, name='facility_propose'),
  path('facility/<int:pk>/', views.FacilityChangeView, name='facility_change'),

  # INFRASTRUCTURE PAGE
  path('infrastructure/', views.InfrastructureView, name='infrastructure'),
  path('infrastructure/complaint/', views.InfrastructureComplaintView, name='infrastructure_complaint'),

  # ABOUT PAGE
  path('about/', views.AboutView, name='about'),

  # GEOAPI
  path('geo-facility/', views.FacilityGeoView, name='geo_facility'),
  path('geo-infrastructure/', views.LineInfrastructureGeoView, name='geo_infrastructure'),
  path('geo-district/', views.DistrictGeoView, name='geo_district'),
  path('geo-complaint/', views.ComplaintGeoView, name='geo_complaint'),
]