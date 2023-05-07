from tourism.models import Profile

def profile(request):
  if request.user.is_authenticated:
    profile = Profile.objects.filter(user=request.user)
    return {'profile': profile}
  else:
    profile = Profile.objects.none()
    return {'profile': profile}