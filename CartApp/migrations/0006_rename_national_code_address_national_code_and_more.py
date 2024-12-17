# Generated by Django 5.1.2 on 2024-12-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CartApp', '0005_discountcode_rename_code_posti_address_national_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='National_code',
            new_name='national_code',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Postal_code',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Unit',
            new_name='unit',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='creat_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Discount (%)'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Code Name'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity Available'),
        ),
    ]
