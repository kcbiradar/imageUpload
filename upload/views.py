from django.shortcuts import render

from django.http import HttpResponse

from . import forms

from . import models

def home(request):
    form = forms.UploadForm()
    return render(request, 'upload/home.html', {
        "form": form
    })
