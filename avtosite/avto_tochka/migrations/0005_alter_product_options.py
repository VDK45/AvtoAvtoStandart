# Generated by Django 4.2.2 on 2023-08-09 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avto_tochka', '0004_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Наименование', 'verbose_name_plural': 'Наименование'},
        ),
    ]
