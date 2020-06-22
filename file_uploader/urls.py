from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
	path('upload/', views.model_form_upload, name='model_form_upload'),
	path('sucess/', views.sucess, name='sucess'),	
]
