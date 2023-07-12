from django import forms

from . import models

class UploadForm(forms.ModelForm):
    class Meta:
        model = models.Upload
        fields = '__all__'
        labels = {'name' : 'Name of the photo' , 'photo' : ''}