# Generated by Django 5.0.1 on 2024-01-28 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'StaffProduct'},
        ),
    ]
