from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'birth_date',
      'phone',
      'address',
      'nationality',
      'avatar'
    ]

    widgets = {
      'birth_date': forms.DateInput(attrs={'type': 'date'}),
    }