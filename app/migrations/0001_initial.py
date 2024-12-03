# Generated by Django 5.1.2 on 2024-12-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255, verbose_name='食品名稱')),
                ('calories', models.FloatField(verbose_name='熱量 (大卡)')),
                ('protein', models.FloatField(verbose_name='蛋白質 (克)')),
                ('sodium', models.FloatField(verbose_name='鈉 (毫克)')),
                ('sugar', models.FloatField(verbose_name='糖 (克)')),
                ('fat', models.FloatField(verbose_name='脂肪 (克)')),
                ('carbohydrates', models.FloatField(verbose_name='碳水化合物 (克)')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='價格 (元)')),
                ('unique_code', models.CharField(blank=True, editable=False, max_length=12, unique=True, verbose_name='編號')),
            ],
            options={
                'verbose_name': '食品資料',
                'verbose_name_plural': '食品資料',
            },
        ),
    ]
