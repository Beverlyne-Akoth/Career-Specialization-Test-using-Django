from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def page1_view(request, *args, **kwargs):
    return render(request, "page1.html", {})

def page2_view(request, *args, **kwargs):
    return render(request, "page2.html", {})

def page3_view(request, *args, **kwargs):
    return render(request, "page3.html", {})

def next1(request, *args, **kwargs):
    return render(request, "page1.html", {})

def next2(request, *args, **kwargs):
    return render(request, "page2.html", {})

def next3(request, *args, **kwargs):
    return render(request, "page3.html", {})