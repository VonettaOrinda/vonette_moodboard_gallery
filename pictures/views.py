from django.shortcuts import render
from django.http import HttpResponse

import gallery

# Create your views here.

def welcome(request):
    return render(request,'all-pictures/welcome.html')


# def home(request):
    # gallery = gallery.objects.all()
    # location = Location.objects.all()
    # category = categories.objects.all()