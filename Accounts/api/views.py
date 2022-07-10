from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

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

class CustomLoginToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            return Response({"response" : "serializer is valid"})
        else:
            return Response({"response" : "serializer is not valid"})
