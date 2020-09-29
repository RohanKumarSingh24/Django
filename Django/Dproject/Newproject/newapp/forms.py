from django import forms
from newapp.models import InputModel

# class InputForm(forms.Form):

# 	FirstName=forms.CharField(max_length=200)
# 	LastName=forms.CharField(max_length=200)
# 	RollNumber=forms.IntegerField(help_text='Enter the 6 digit roll number')
# 	Password=forms.CharField(widget=forms.PasswordInput())


class InputForm(forms.ModelForm):

	class Meta():

		model=InputModel
		widgets={'Password':forms.PasswordInput()}
		
		fields='__all__'