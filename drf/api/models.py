from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description =  models.TextField(max_length=700)
	author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Profile(models.Model):
	GENDER_CHOICES = (
		('m', 'Male'),
		('f', 'Female'),
		('a', 'Anonymous')
	)


	user = models.ForeignKey(User, on_delete=models.CASCADE)
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=35)

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	status = models.CharField(max_length=20)

	bio = models.TextField(max_length=500)

	def __str__(self):
		return self.user.username

