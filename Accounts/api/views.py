from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data["token"] = Token.objects.get(user=user).key
        data["username"] = user.username
        data["email"] = user.email
    else:
        data = serializer.errors
    return Response(data)