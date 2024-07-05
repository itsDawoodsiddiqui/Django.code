from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def brian(request):
    return HttpResponse("Hello Brian!")

def david(request):
    return HttpResponse("Hello David")

def greet(request, name):
    return render(request, "hello/index.html", {
        "name": name.capitalize()
    })