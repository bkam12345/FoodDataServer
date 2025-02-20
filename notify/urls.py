from django.urls import path
from . import views

urlpatterns = [
    path('notify/add/', views.addNotify, name='addNotify'),
    path('notify/customMessage/', views.customMessage, name='addNotify'),
]
