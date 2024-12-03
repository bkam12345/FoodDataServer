from django.db import models

class FoodData(models.Model):
    food_name = models.CharField(max_length=255, verbose_name="食品名稱")
    calories = models.FloatField(verbose_name="熱量 (大卡)")
    protein = models.FloatField(verbose_name="蛋白質 (克)")
    sodium = models.FloatField(verbose_name="鈉 (毫克)")
    sugar = models.FloatField(verbose_name="糖 (克)")
    fat = models.FloatField(verbose_name="脂肪 (克)")
    carbohydrates = models.FloatField(verbose_name="碳水化合物 (克)")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="價格 (元)")
    unique_code = models.CharField(max_length=12, unique=True, blank=True, editable=False, verbose_name="編號")

    def save(self, *args, **kwargs):
        if not self.unique_code:
            import uuid
            self.unique_code = f"FD{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.food_name} ({self.unique_code})"

    class Meta:
        verbose_name = "食品資料"
        verbose_name_plural = "食品資料"
