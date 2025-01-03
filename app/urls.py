from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data/<str:unique_code>/', views.get_food_data, name='get_food_data'),
]
