from django.contrib import admin
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiration_date')
    search_fields = ('name',)
    list_filter = ('expiration_date',)
