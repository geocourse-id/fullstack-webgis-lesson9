from django.shortcuts import render
from .forms import Register

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