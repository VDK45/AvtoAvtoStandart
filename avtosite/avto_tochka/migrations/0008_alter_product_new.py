# Generated by Django 4.2.2 on 2023-08-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto_tochka', '0007_product_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, verbose_name='Новая запчасть'),
        ),
    ]
