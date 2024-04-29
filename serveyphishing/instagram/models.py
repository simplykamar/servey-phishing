from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=30)
	passwd = models.CharField(max_length=30)

	def __str__(self):
		return self.email