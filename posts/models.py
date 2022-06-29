from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    desctiption = models.TextField()
    author = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='/media/%Y/%m/%d/',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title