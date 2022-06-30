from dataclasses import field
from rest_framework.serializers import Serializer, ModelSerializer

from ..models import Post

class PostSerializer(ModelSerializer): # you can use usual Seruializer class :: don't forget to write create and update functions
    class Meta:
        model = Post
        fields = ["title", "author", "created"]