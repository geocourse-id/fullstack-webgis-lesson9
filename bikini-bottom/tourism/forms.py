from django import forms
from .models import Booking, Facility, Complaint, Review
from django.contrib.admin import widgets
from leaflet.forms.widgets import LeafletWidget

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

class BookingCancelForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = [
      'payment_status',
      'user'
    ]

    widgets = {
      'payment_status': forms.TextInput(attrs={'readonly': True}),
      'user': forms.TextInput(attrs={'hidden': True}),
    }

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
      'status': forms.TextInput(attrs={'readonly': True}),
      'operator': forms.TextInput(attrs={'hidden': True})
    }

class FacilityBookedConfirmForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ['payment_status']

    widgets = {
      'payment_status': forms.TextInput(attrs={'readonly': True}),
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
      'specific_location': forms.TextInput(attrs={'readonly': True}),
    }

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = [
      'booking',
      'score',
      'comment',
    ]

    widgets = {
      'booking': forms.TextInput(attrs={'readonly': True}),
    }

  def __init__(self, *args, **kwargs):
    super(ReviewForm, self).__init__(*args, **kwargs)
    self.fields['booking'].label = 'Booking ID'