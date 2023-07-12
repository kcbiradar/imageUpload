from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Learning image upload in django </h1>")
