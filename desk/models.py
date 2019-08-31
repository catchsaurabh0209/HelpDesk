from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
	author=models.CharField(max_length=50)
	question=models.CharField(max_length=200)
	answer=models.CharField(max_length=400)
	created_date=models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.author

