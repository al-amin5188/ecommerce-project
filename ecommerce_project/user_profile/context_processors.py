from .models import Profile

def profile_info(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()  
        return {'profile': profile}  
    return {}