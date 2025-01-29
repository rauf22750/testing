from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')
