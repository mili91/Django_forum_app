from django.shortcuts import render

def register(request):
    return render(request, 'user_profile/register.html')

def profile(request):
    return render(request, 'user_profile/profile.html')