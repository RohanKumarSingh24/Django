from django.shortcuts import render
from newapp.forms import InputForm

# Create your views here.

def index(request):

	context={}
	context['form']=InputForm()

	return render(request,'newapp/index.html',context)

