# Generated by Django 5.1.2 on 2024-11-14 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='last_send',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]