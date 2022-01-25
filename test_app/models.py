from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.title

