from django.db import models

# Create your models here.

class Record(models.Model):

	name=models.CharField(max_length=200)
	email=models.EmailField()
	verify_email=models.EmailField()
	text=models.CharField(max_length=300)

