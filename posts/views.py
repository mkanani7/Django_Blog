from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import Post
from .forms import CommentForm
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

# function based view can be good for detail view below.(there is duplicate codes in classBased view)
class PostDetailView(View):
    def get(self, request, post_id):
        context = {}
        comment_form = CommentForm()
        post = get_object_or_404(Post, id=post_id)
        context['post'] = post
        context['comments'] = post.comments.all()
        context['comment_form'] = comment_form
        
        return render(request, 'post/detail.html', context=context)

    def post(self, request, post_id):
        context = {}
        comment_form = CommentForm(data=request.POST)
        post = get_object_or_404(Post, id=post_id)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
        context['comment_form'] = comment_form
        context['comments'] = post.comments.all()
        

        return render(request, 'post/detail.html', context=context)