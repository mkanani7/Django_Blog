from django.urls import path

from .views import register_user, CustomLoginToken

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', register_user),
    path('login', CustomLoginToken.as_view(), name="login"),
]