from django.shortcuts import render

from django.http import HttpResponse

from . import forms

from . import models

def home(request):
    if request.method == "POST":
        form = forms.UploadForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()
    form = forms.UploadForm()
    data = models.Upload.objects.all()
    return render(request, 'upload/home.html', {
        "form": form,
        "data" : data
    })
