from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiration_date')
    search_fields = ('name',)
    list_filter = ('expiration_date',)
