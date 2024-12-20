# Generated by Django 5.1.2 on 2024-11-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0004_alter_product_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='creat_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='capsule_in_claw',
            field=models.BooleanField(default=False, verbose_name='کپسول فشار در قسمت پنجه '),
        ),
        migrations.AlterField(
            model_name='product',
            name='capsule_in_heel',
            field=models.BooleanField(default=False, verbose_name='کپسول فشار در قسمت پاشنه'),
        ),
    ]
