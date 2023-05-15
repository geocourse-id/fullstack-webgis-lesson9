from django.shortcuts import render, redirect, get_object_or_404
from .forms import Register, ProfileForm
from .models import Profile

def RegisterView(request):
  if request.method == 'POST':
    user_form = Register(request.POST)

    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
      return render(request, 'registration/register_done.html', {'form': user_form})
    
  else:
    user_form = Register()

  return render(request, 'registration/register.html', {'form': user_form})

def ProfileView(request):
  return render(request, 'accounts/profile.html')

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
  return render(request, 'accounts/profile_add.html', {'form': form})

def ProfileUpdateView(request, pk):
  item = get_object_or_404(Profile, user=pk)
  form = ProfileForm(request.POST or None, request.FILES or None, instance=item)
  if request.method == 'POST':
    if form.is_valid():
      item.user = request.user
      form.save()
      return redirect('profile')
  return render(request, 'accounts/profile_update.html', {'form': form})