from django import forms
from .models import Profile, Booking, Facility, Complaint
from django.contrib.admin import widgets
from leaflet.forms.widgets import LeafletWidget

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'birth_date',
      'phone',
      'address',
      'nationality',
      'avatar',
      'user',
    ]

    widgets = {
      'birth_date': forms.DateInput(attrs={'type': 'date'}),
      'user': forms.TextInput(attrs={'hidden': True})
    }

class BookingForm(forms.ModelForm):
  start_visit = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
  end_visit = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
  
  class Meta:
    model = Booking
    fields = [
      'facility',
      'start_visit',
      'end_visit',
      'payment_method',
    ]

class FacilityProposeForm(forms.ModelForm):
  class Meta:
    model = Facility
    fields = [
      'name',
      'types',
      'location',
      'price',
      'price_unit',
      'photo',
    ]

    LEAFLET_WIDGET_ATTRS = {
      'map_height': '500px',
      'map_width': '100%',
      'map_srid': 4326,
    }

    widgets = {
      'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)
    }

class FacilityChangeForm(forms.ModelForm):
  class Meta:
    model = Facility
    fields = ['name', 'open', 'price', 'price_unit', 'photo', 'status', 'operator']

    widgets = {
      'status': forms.TextInput(attrs={'disabled': True}),
      'operator': forms.TextInput(attrs={'hidden': True})
    }

class InfrastructureComplaintForm(forms.ModelForm):
  class Meta:
    model = Complaint
    fields = [
      'infrastructure',
      'types',
      'specific_location',
      'proof_image',
      'comment'
    ]

    widgets = {
      'specific_location': forms.TextInput(attrs={'disabled': True}),
    }