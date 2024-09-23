from django.db import models

# Create your models here.
class pi(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	mobile=models.CharField(max_length=40)
	course=course.CharField(max_length=40)
