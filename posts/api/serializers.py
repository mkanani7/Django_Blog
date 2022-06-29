from dataclasses import field
from rest_framework.serializers import Serializer, ModelSerializer

from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "author", "created"]