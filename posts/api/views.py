from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from ..models import Post

class PostViewSet(ModelViewSet): # you can use APIView or even function base view for this view.
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticated,]
