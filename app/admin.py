from django.contrib import admin
from .models import FoodData

@admin.register(FoodData)
class FoodDataAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'food_name', 'calories', 'protein', 'sodium', 'sugar', 'fat', 'carbohydrates', 'price')
    search_fields = ('food_name', 'unique_code')
    list_filter = ('calories', 'protein', 'sodium', 'sugar', 'fat', 'carbohydrates', 'price')
    readonly_fields = ('unique_code',)
    ordering = ('food_name',)

    fieldsets = (
        (None, {
            'fields': ('food_name', 'calories', 'protein', 'sodium', 'sugar', 'fat', 'carbohydrates', 'price', 'unique_code'),
        }),
    )
