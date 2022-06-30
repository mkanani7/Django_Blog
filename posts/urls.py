from django.urls import path, include

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('post/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail')
]