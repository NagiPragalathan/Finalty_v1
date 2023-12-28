from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")

def ContactUs(request):
    return render(request,"contact.html")

def team(request):
    return render(request, "team.html")

def services(request):
    return render(request, "service.html")

def underdev(request):
    return render(request, "underdev.html")
