from django.contrib.gis import admin
from .models import Facility

class LocationAdmin(admin.OSMGeoAdmin):
  default_zoom = 11
  default_lon = 18409015.29
  default_lat = 1300740.59

admin.site.register(Facility, LocationAdmin)