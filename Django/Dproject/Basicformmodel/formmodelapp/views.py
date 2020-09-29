from django.shortcuts import render
from formmodelapp.forms import Formmodel
from formmodelapp import forms


# Create your views here.

def index(request):

	return render(request,'formmodelapp/index.html')


def userformmodel(request):

	form=Formmodel()

	if request.method =='POST':

		form=Formmodel(request.POST)

		if form.is_valid():

			form.save(commit=True)
			return index(request)

		else:

			print("ERROR")

	return render(request,'formmodelapp/form_model.html',{'form':form})		
		







