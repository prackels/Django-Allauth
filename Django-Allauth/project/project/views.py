from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def profile(request):
    return render(request, 'profile.html')
