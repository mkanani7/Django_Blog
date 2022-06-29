from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .serializers import PostSerializer
from ..models import Post

class PostListView(ListAPIView): # you can use APIView or even function base view for this view.
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
