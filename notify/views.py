from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodForm
from .utils import send_line_notify

@login_required
def addNotify(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            message = f"成功新增食物：{food.name}，到期日：{food.expiration_date}"
            send_line_notify(message)
            return redirect('addNotify')
    else:
        form = FoodForm()
    return render(request, 'addNotify.html', {'form': form})