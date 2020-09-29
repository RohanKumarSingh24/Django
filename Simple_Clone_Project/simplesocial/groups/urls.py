from django.urls import path,re_path

from django.contrib.auth import views as auth_views

from groups import views

app_name='groups'


urlpatterns=[
	re_path(r'^$',views.ListGroup.as_view(),name='all'),
	re_path(r'^new/$',views.CreateGroup.as_view(),name='create'),
	re_path(r'post/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
	re_path(r'join/(?P<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),
	re_path(r'leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave'),
	

]