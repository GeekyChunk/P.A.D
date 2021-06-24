from django.urls import path
from .views import *

urlpatterns = [
	path('user/', CurrentUserView.as_view(), name="register"),
	path('todo/', TodoList.as_view(), name="list"),
	path('todo/create', TodoCreate.as_view(), name="create"),
	path('todo/<slug:slug>/', TodoDetail.as_view()),
	path('todo/<slug:slug>/update/', TodoUpdate.as_view()),
	path('test/', test)
]