from rest_framework.decorators import api_view
from django.contrib.auth.models import *
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import *
from .models import *

# Views

class IsAuthor(BasePermission):

	def has_object_permission(self, request, view, obj):
	    return bool(obj.author == request.user)

class IsUser(BasePermission):

	def has_object_permission(self, request, view, obj):
	    return bool(obj == request.user)

# class UserCreateList(ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	permission_classes = (IsAuthenticated,)

class CurrentUserView(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)

	def get_object(self, usr):
		user = User.objects.get(id=usr.id)
		return Profile.objects.get(user=user)

	def get(self, request):
		snippet = self.get_object(request.user)
		serializer = ProfSerializer(snippet)

		return Response({"user": serializer.data})

	def put(self, request):
		snippet = self.get_object(request.user)
		serializer = ProfSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors)

class TodoList(ListAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class TodoCreate(CreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoCreateSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class TodoDetail(RetrieveAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	lookup_field = 'slug'

class TodoUpdate(RetrieveUpdateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoUpdateSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	lookup_field = 'slug'
	permission_classes = (IsAuthor,)


@api_view()
def test(request):
    return Response({"username": str(request.user.username)})


# class WUser(RetrieveAPIView):
# 	serializer_class = TodoSerializer
# 	permission_classes = [IsAuthenticated]

# 	def get_queryset(self):
# 		pass

# 	lookup_field = 'slug'