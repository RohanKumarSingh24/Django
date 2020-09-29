from django.conf.urls import url
from basicapp  import views


urlpatterns=[
	url(r'^$',views.form_page_view,name='form_page_view')
]