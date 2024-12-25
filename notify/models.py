from django.db import models
from django.utils.timezone import now

class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name="食物名稱")
    expiration_date = models.DateField(verbose_name="到期時間")
    notified_expiring = models.BooleanField(default=False, verbose_name="已通知即將過期")
    notified_expired = models.BooleanField(default=False, verbose_name="已通知過期")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "食物"
        verbose_name_plural = "食物清單"
        ordering = ['expiration_date']

    def is_expiring_soon(self):
        return (self.expiration_date - now().date()).days <= 3

    def is_expired(self):
        return now().date() > self.expiration_date
