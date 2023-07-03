# Generated by Django 4.2.2 on 2023-07-03 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avto_tochka', '0003_category_service_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории услуг', 'verbose_name_plural': 'Категории услуг'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категории услуг'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='avto_tochka.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Обпуликовать'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.SmallIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='service',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='service',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
