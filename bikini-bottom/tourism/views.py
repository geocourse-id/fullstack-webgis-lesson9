from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Facility, LineInfrastructure, District, Profile
from .forms import ProfileForm

def HomeView(request):
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

def ProfileView(request):
  return render(request, 'tourism/profile.html')

def ProfileAddView(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit=False)
      item.user = request.user
      item.save()
      return redirect('profile')
  else:
    form = ProfileForm()
  return render(request, 'tourism/profile_add.html', {'form': form})

def ProfileUpdateView(request, pk):
  item = get_object_or_404(Profile, user=pk)
  form = ProfileForm(request.POST or None, request.FILES or None, instance=item)
  if request.method == 'POST':
    if form.is_valid():
      item.user = request.user
      form.save()
      return redirect('profile')
  return render(request, 'tourism/profile_update.html', {'form': form})