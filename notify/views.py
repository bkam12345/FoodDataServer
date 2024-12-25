from django.shortcuts import render, redirect
from .forms import FoodForm
from .utils import send_line_notify

def home(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            message = f"成功新增食物：{food.name}，到期日：{food.expiration_date}"
            send_line_notify(message)
            return redirect('home')
    else:
        form = FoodForm()
    return render(request, 'home.html', {'form': form})