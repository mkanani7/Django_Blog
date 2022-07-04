from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2' ]

    def save(self):
        vd = self.validated_data
        user = User(email = vd['email'], username = vd['username'], first_name = vd['first_name'], last_name=vd['last_name'])
        if vd['password'] != vd['password2']:
            raise serializers.ValidationError({'password' : 'passwords must match!!'})
        user.set_password(vd['password'])
        user.save()
        return user