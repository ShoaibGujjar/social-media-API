from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser,UserImage
from rest_framework.validators import UniqueValidator


class UserImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserImage
        fields=[
            'fbId',
            'image'
            ]

class CustomUserSerializer(serializers.ModelSerializer):
    userimage=UserImagesSerializer(many=True)
    class Meta:
        model=CustomUser
        fields=[
            'firstName',
            'lastName',
            'age',
            'gender',
            'jobTitle',
            'school',
            'fbId',
            'birthday',
            'userimage'
        ]

class addUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

