# Generated by Django 5.1.4 on 2024-12-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='notified_expired',
            field=models.BooleanField(default=False, verbose_name='已通知過期'),
        ),
        migrations.AddField(
            model_name='food',
            name='notified_expiring',
            field=models.BooleanField(default=False, verbose_name='已通知即將過期'),
        ),
    ]