from django.urls import path,re_path
from formmodelapp import views


urlpatterns=[
	re_path(r'^$',views.userformmodel, name='userformmodel')

]

