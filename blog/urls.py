from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # our API urls
    path('api/', include('posts.api.urls')),
    path('api/users/', include('Accounts.api.urls')),

    path('', include('posts.urls', namespace='posts')),
    path('users/', include('Accounts.urls')),
]
