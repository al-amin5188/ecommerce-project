from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def profile_redirect(request):   
    if request.user.is_authenticated:
        return redirect('profile-view')
    else:
        return redirect('login')


# Profile views
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    context={
        'profile':profile,
    }
    return render(request, 'user_profile/profile.html',context)

# Profile details 
@login_required
def profile_details(request):
    profile = Profile.objects.get(user=request.user)
    context={
        'profile':profile,
    }
    return render (request,'user_profile/profile_details.html',context)

#Edite Profile 
@login_required
def edite_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Handling the uploaded profile picture and other form data
        profile_pic = request.FILES.get('profile-pic')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')

        # Update profile information
        profile.user.first_name = first_name
        profile.user.last_name = last_name
        profile.phone_number = phone_number
        profile.address = address
        
        if profile_pic:
            profile.profile_picture = profile_pic
        
        profile.user.save()  
        profile.save()  

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile-view') 


#Edite Profile Views
@login_required
def edite_profile_page(request):
    profile = Profile.objects.get(user=request.user)
    context={
        'profile':profile,
    }
    return render (request, 'user_profile/edite_profile.html', context)

# Profile Sitting 

def sitting_page(request):
    return render(request,'user_profile/sitting_page.html')