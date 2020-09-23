from django.urls import path
from . import views

urlpatterns = [
	path('', views.bottle_list, name='bottle_list'),
]