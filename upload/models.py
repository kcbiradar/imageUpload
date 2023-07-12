from django.db import models

class Upload(models.Model):
    name = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to="media/myimage")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


