from django import forms
from django.contrib.auth.models import User
from .models import Profile

class Register(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

    widgets = {
      'first_name': forms.TextInput(attrs={'required': True}),
      'last_name': forms.TextInput(attrs={'required': True}),
      'email': forms.TextInput(attrs={'required': True}),
    }

  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  re_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

  def clean_re_password(self):
    cd = self.cleaned_data
    if cd['password'] != cd['re_password']:
      raise forms.ValidationError('Password don\'t match')
    
    return cd['re_password']
  
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'birth_date',
      'phone',
      'address',
      'nationality',
      'avatar',
    ]

    widgets = {
      'birth_date': forms.DateInput(attrs={'type': 'date'})
    }