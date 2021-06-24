from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TodoSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Todo
        exclude = ['id']
        read_only_fields = ('author', )

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description']

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'slug', 'created', 'author']
        read_only_fields = ('author',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_active', 'groups', 'user_permissions', 'date_joined', 'is_staff', 'is_superuser']



class ProfSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()

    class Meta:
        model = Profile
        exclude = ['id']
