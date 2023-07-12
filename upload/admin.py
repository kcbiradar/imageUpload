from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'photo' ,'date']
