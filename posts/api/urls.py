from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
]
