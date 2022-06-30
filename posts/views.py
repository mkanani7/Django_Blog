from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import Post

# function based view

# def post_list(request):
#     context = {}
#     posts = Post.objects.all()
#     context['posts'] = posts
#     return render(request, 'post/list.html', context=context)

# class based view
class PostListView(ListView):
    template_name = 'post/list.html'
    def get_queryset(self):
        return Post.objects.all()
    
    def get_context_data(self):
        return {'posts': Post.objects.all()}

class PostDetailView(View):
    def get(self, request, post_id):
        context = {}
        post = get_object_or_404(Post, id=post_id)
        context['post'] = post
        return render(request, 'post/detail.html', context=context)