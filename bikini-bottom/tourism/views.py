from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Facility, LineInfrastructure, District
import json

def FacilityView(request):
  return render(request, 'tourism/home.html')

def FacilityGeoView(request):
  place = serialize('geojson', Facility.objects.all())
  return HttpResponse(place, content_type='json')

def LineInfrastructureGeoView(request):
  place = serialize('geojson', LineInfrastructure.objects.all())
  return HttpResponse(place, content_type='json')

def DistrictGeoView(request):
  place = serialize('geojson', District.objects.all())
  return HttpResponse(place, content_type='json')
