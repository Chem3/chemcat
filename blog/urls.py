from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.bottle_list, name='bottle_list'),
    path('bottle/<int:pk>/', views.bottle_detail, name='bottle_detail'),
    path('search/', SearchResultsView.as_view(), name='bottle_search'),
    path('shelf/<str:shortname>', views.shelf_detail, name='shelf_detail'),
]