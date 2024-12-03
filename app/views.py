from django.shortcuts import render
from .models import FoodData
from django.http import JsonResponse

def get_food_data(request, unique_code):
    try:
        food = FoodData.objects.get(unique_code=unique_code)
        data = {
            "food_name": food.food_name,
            "calories": food.calories,
            "protein": food.protein,
            "sodium": food.sodium,
            "sugar": food.sugar,
            "fat": food.fat,
            "carbohydrates": food.carbohydrates,
            "price": float(food.price),
            "unique_code": food.unique_code,
        }
        return JsonResponse(data)
    except FoodData.DoesNotExist:
        return JsonResponse({"error": "Food data not found"}, status=404)