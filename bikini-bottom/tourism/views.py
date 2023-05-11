from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Facility, LineInfrastructure, District, Profile, Booking, Complaint, Review
from .forms import ProfileForm, BookingForm, FacilityProposeForm, FacilityChangeForm, InfrastructureComplaintForm, ReviewForm
from django.db.models import Avg

def HomeView(request):
  context = {
    'data': Review.objects.select_related('booking').values('booking__facility').annotate(avg_score=Avg('score'))
  }
  return render(request, 'tourism/home.html', context)

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

def BookingView(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      item = form.save(commit=False)
      item.user = request.user
      item.save()
      return redirect('booking')
  else:
    form = ReviewForm()

  context = {
    'booking': Booking.objects.filter(user=request.user).select_related('review'),
    'form': form
  }
  return render(request, 'tourism/booking.html', context)

def BookingAddView(request):
  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      item = form.save(commit=False)
      item.user = request.user
      item.save()
      return redirect('booking')
  else:
    form = BookingForm()
  return render(request, 'tourism/booking_add.html', {'form': form})

def FacilityView(request):
  context = {
    'facility': Facility.objects.filter(operator=request.user)
  }
  return render(request, 'tourism/facility.html', context)

def FacilityProposeView(request):
  if request.method == 'POST':
    form = FacilityProposeForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit=False)
      item.operator = request.user
      item.save()
      return redirect('facility')
  else:
    form = FacilityProposeForm()
  return render(request, 'tourism/facility_propose.html', {'form': form})

def FacilityChangeView(request, pk):
  item = get_object_or_404(Facility, pk=pk)
  form = FacilityChangeForm(request.POST or None, request.FILES or None, instance=item)
  if request.method == 'POST':
    if form.is_valid():
      item.operator = request.user
      form.save()
      return redirect('facility')
  return render(request, 'tourism/facility_change.html', {'form': form})

def InfrastructureView(request):
  context = {
    'complaint': Complaint.objects.filter(user=request.user)
  }
  return render(request, 'tourism/infrastructure.html', context)

def ComplaintGeoView(request):
  place = serialize('geojson', Complaint.objects.filter(user=request.user))
  return HttpResponse(place, content_type='json')

def InfrastructureComplaintView(request):
  if request.method == 'POST':
    form = InfrastructureComplaintForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit=False)
      item.user = request.user
      item.save()
      return redirect('infrastructure')
  else:
    form = InfrastructureComplaintForm()
  return render(request, 'tourism/infrastructure_complaint.html', {'form': form})