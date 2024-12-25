from django import forms
from .models import FoodItem

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': '食物名稱',
            'expiration_date': '到期日期',
        }
