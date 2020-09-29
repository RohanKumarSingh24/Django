from django import forms
from django.core import validators
from formmodelapp.models import Record



class Formmodel(forms.ModelForm):

	class Meta():

		model=Record
		fields='__all__'

	def clean(self):

		all_clean_data=super().clean()

		
		email=all_clean_data['email']
		verify_email=all_clean_data['verify_email']
	

		if email != verify_email:

			raise forms.ValidationError("Make Sure Email Match!")


		