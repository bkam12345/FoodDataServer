from celery import shared_task
from django.utils.timezone import now
from notify.models import FoodItem

@shared_task
def check_expiring_and_expired_foods():
    expiring_soon_items = FoodItem.objects.filter(
        expiration_date__gt=now().date(),
        expiration_date__lte=now().date() + timedelta(days=3),
        notified_expiring=False
    )

    expired_items = FoodItem.objects.filter(
        expiration_date__lte=now().date(),
        notified_expired=False
    )

    for item in expiring_soon_items:
        send_notification(item, "即將過期通知")
        item.notified_expiring = True
        item.save()

    for item in expired_items:
        send_notification(item, "過期通知")
        item.notified_expired = True
        item.save()

def send_notification(food_item, message):
    print(f"發送通知給 {food_item.name}：{message}")
