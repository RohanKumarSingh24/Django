from django.shortcuts import render
from django.http import HttpResponse
from firstAPP.models import Topic,AccessRecord,Webpage

# Create your views here.
# def index(request):
# 	return HttpResponse("Hello World")

# def index(request):
# 	dict={'insert_me':' Hello This is from views.py'}

# 	return render(request,'index.html',context=dict)

# def index(request):	

# 	dict={'insert_me':'Now I am coming from firstAPP/index.html'}
# 	return render(request,'firstAPP/index.html',context=dict)

def index(request):

	webpage_list=AccessRecord.objects.order_by('date')
	date_dict={"access_records":webpage_list}
	return render(request,'firstAPP/index.html',context=date_dict)