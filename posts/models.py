from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    desctiption = models.TextField()
    author = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/%Y/%m/%d',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    msg = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id