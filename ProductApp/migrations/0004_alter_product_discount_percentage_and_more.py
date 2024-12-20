# Generated by Django 5.1.2 on 2024-11-17 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0003_alter_color_color_alter_insolemodel_insole_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='تخفیف (%)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery_image',
            field=models.ManyToManyField(related_name='product', to='ProductApp.productgallery', verbose_name='گالری'),
        ),
    ]
