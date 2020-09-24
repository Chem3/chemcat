from django.urls import path
from . import views

urlpatterns = [
    path('', views.bottle_list, name='bottle_list'),
    path('bottle/<int:pk>/', views.bottle_detail, name='bottle_detail'),
    path('search/', views.bottle_search, name='bottle_search'),
]