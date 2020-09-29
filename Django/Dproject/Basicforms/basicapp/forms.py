from django import forms
from django.core import validators
#from basicapp.models import Record

# class FormName(forms.Form):

# 	name=forms.CharField()
# 	email=forms.EmailField()
# 	text=forms.CharField(widget=forms.Textarea)

# In case of Botcatcher

# class FormName(forms.Form):

# 	name=forms.CharField()
# 	email=forms.EmailField()
# 	text=forms.CharField(widget=forms.Textarea)
# 	botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)


# 	#validating inside class using clean function()

# 	def clean_botcatcher(self):

# 		botcatcher=self.cleaned_data['botcatcher']

# 		if len(botcatcher) > 0 :

# 			raise forms.ValidationError("GOT BOT CATCH!")

# 		return botcatcher 	

# using Django Validators inside particual field in class attributes

# class FormName(forms.Form):

# 	name=forms.CharField()
# 	email=forms.EmailField()
# 	text=forms.CharField(widget=forms.Textarea)
# 	botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
# 							   validators=[validators.MaxLengthValidator(0)])


# Create own custom validator for particular field of Class


# def check_for_z(value):

# 	if value[0].lower() != 'z':

# 		raise forms.ValidationError("Need To Be Start with z")
	
# 	return	


# class FormName(forms.Form):

# 	name=forms.CharField(validators=[check_for_z])
# 	email=forms.EmailField()
# 	text=forms.CharField(widget=forms.Textarea)
# 	botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
# 							   validators=[validators.MaxLengthValidator(0)])

# Clean the entire form 

class FormName(forms.Form):

	name=forms.CharField()
	email=forms.EmailField()
	verify_email=forms.EmailField(label="Enter your email again :")
	text=forms.CharField(widget=forms.Textarea)
	

	def clean(self):

		all_clean_data=super().clean()
		email=all_clean_data['email']
		vmail=all_clean_data['verify_email']

		if email != vmail:

			raise forms.ValidationError("Make sure email is match!")



# if we want to save any data from form page to directly into database in this we write a funtion like that:
# class FormName(forms.ModelForm):

# 	class Meta():
# 		model=Record
# 		fields = '__all__'
	

# 	def clean(self):

# 		all_clean_data=super().clean()
# 		email=all_clean_data['email']
# 		vmail=all_clean_data['verify_email']

# 		if email != vmail:

# 			raise forms.ValidationError("Make sure email is match!")


							   

