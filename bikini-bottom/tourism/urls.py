from django.urls import path
from .views import FacilityView, FacilityGeoView, LineInfrastructureGeoView, DistrictGeoView

urlpatterns = [
  path('', FacilityView, name='home'),
  path('geo-facility/', FacilityGeoView, name='geo_facility'),
  path('geo-infrastructure/', LineInfrastructureGeoView, name='geo_infrastructure'),
  path('geo-district/', DistrictGeoView, name='geo_district'),
]