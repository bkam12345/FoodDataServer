from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notify.urls')),
    path('data/<str:unique_code>/', views.get_food_data, name='get_food_data'),
]
