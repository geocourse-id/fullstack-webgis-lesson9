from django import forms
from django.contrib.auth.models import User

class Register(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  re_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

  def clean_re_password(self):
    cd = self.cleaned_data
    if cd['password'] != cd['re_password']:
      raise forms.ValidationError('Password don\'t match')
    
    return cd['re_password']