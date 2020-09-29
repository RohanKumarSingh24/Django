from django.db import models

# Create your models here.

class InputModel(models.Model):

	FirstName=models.CharField(max_length=200)
	LastName=models.CharField(max_length=200)
	RollNumber=models.IntegerField(help_text='Enter the 6 digit roll number')
	Password=models.CharField(max_length=50)


	def __str__(self):

		return self.RollNumber




