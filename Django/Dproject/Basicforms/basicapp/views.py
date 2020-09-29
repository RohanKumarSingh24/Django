from django.shortcuts import render
from basicapp import forms
from basicapp.forms import FormName


# Create your views here.

def index(request):

	return render(request,'basicapp/index.html')


# def users(request):
# 	form=FormName()

# 	if request.method=="POST":

# 		form=FormName(request.POST)

# 		if form.is_valid():

# 			form.save(commit=True)
# 			return index(request)

# 		else:

# 			print("ERROR")
# 	return render(request,"basicapp/form_page.html",{'form':form})		
			




def form_page_view(request):
	form=forms.FormName()

	if request.method=='POST':
		form=forms.FormName(request.POST)

		if form.is_valid():
			print("VALIDATION IS SUCCESSFUL!")

			print("NAME :"+form.cleaned_data['name'])
			print("EMAIL :"+form.cleaned_data['email'])
			print("TEXT :"+form.cleaned_data['text'])

	return render (request,'basicapp/form_page.html',{'form':form})





          

