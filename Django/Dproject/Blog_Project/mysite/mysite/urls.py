"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from blog import views
from django.contrib.auth import views as auth_view 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'',include('blog.urls')),
 	#re_path(r'accounts/login/$',views.login,name='login'),
 	re_path(r'^accounts/login/', LoginView.as_view(), name='login'),
 	#re_path(r'^accounts/login/$',LoginView.as_view(template_name='blog/registration/login.html'),name='login'),
 	re_path(r'^accounts/logout/$',LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),
]
