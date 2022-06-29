from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from ..models import Post

class PostListView(ListAPIView): # you can use APIView or even function base view for this view.
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


class PostDetailView(APIView):

    def get(self, request, pk, format=None):
        try:
            post = get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(post)
        serializer = PostSerializer(post)
        print(serializer)
        return Response(serializer.data)
        
    def post(self, request, pk, format=None):
        try:
            post = get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
