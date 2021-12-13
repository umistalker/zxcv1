from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_data_view, name='get_data_view'),
    path('show_data_view/', views.show_data_view, name='show_data_view')
]
