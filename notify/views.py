from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodForm
from .utils import send_notify
import asyncio

@login_required
def addNotify(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            message = f"成功新增食物：{food.name}，到期日：{food.expiration_date}"
            asyncio.run(send_notify(message))
            return redirect('addNotify')
    else:
        form = FoodForm()
    return render(request, 'addNotify.html', {'form': form})


@login_required
def customMessage(request):
    message_sent = False
    if request.method == 'POST':
        message = request.POST.get("message", "").strip()
        if message:
            asyncio.run(send_notify(message))
            message_sent = True
    return render(request, 'customMessage.html', {"message_sent": message_sent})