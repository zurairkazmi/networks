from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import Ad
import datetime

def index(request):
    age = request.GET.get('age')
    gender = request.GET.get('gender')
    country = request.GET.get('country')
    if(age):
        if( int(age) > 16):
            latest_ad_list = Ad.objects.filter(age_rating__gt=18, validity_date__gte=datetime.date.today()).order_by('-id')[:5]
        else:
            latest_ad_list = Ad.objects.filter(age_rating__lt=18, validity_date__gte=datetime.date.today()).order_by('-id')[:5]
    elif(gender):
        latest_ad_list = Ad.objects.filter(gender_rating=gender, validity_date__gte=datetime.date.today()).order_by('-id')[:5]
    elif(country):
        latest_ad_list = Ad.objects.filter(country_id=country, validity_date__gte=datetime.date.today()).order_by('-id')[:5]
    else:
        latest_ad_list = Ad.objects.filter(validity_date__gte=datetime.date.today()).order_by('-id')[:5]  
    context = {'latest_ad_list': latest_ad_list}
    return render(request, 'ads/index.html', context)

def logout_view(request):
    logout(request)
    return(redirect('/admin'))