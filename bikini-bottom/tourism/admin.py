from django.contrib.gis import admin
from .models import Facility, Booking, Review, Profile, LineInfrastructure, Complaint, District

class LocationAdmin(admin.OSMGeoAdmin):
  default_zoom = 11
  default_lon = 18409015.29
  default_lat = 1300740.59

@admin.register(Facility)
class FacilityAdmin(LocationAdmin):
  list_filter = ['name', 'status']
  list_display = ['id', 'name', 'status']

@admin.register(Complaint)
class ComplaintAdmin(LocationAdmin):
  list_filter = ['types', 'status_handling']
  list_display = ['id', 'infrastructure', 'types', 'status_handling']

admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(LineInfrastructure, LocationAdmin)
admin.site.register(District, LocationAdmin)