from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy




class TestPage(TemplateView):

	template_name='test.html'



class ThanksPage(TemplateView):

	template_name='thanks.html'

	
class HomePage(TemplateView):

	template_name='index.html'



	# def get(self, request, *args, **kwargs):

	# 	try:
	# 		if request.user.is_authenticated():

	# 			return HttpResponseRedirect(reverse("test"))

	# 		return super().get(request, *args, **kwargs)