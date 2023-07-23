from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.SmallIntegerField(default=0, verbose_name='Цена')
    content = models.TextField(blank=False, verbose_name='Описание')  # Пустое = False
    # Нужно установить pillow

    # Нужно добавить в seting.py
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # MEDIA_URL = '/media/'

    # Нужно добавить в avtosite\url.py
    # if settings.DEBUG:  # import from avtosite
    #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')  # Загрузить в "photos/%Y/%m/%d/"
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Обпуликовать')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')  # (cat)_id автоматом добавится

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


# in terminal: python manage.py makemigrations
# Show sql command: python manage.py sqlmigrate avto_tochka 0001
# Create table: python manage.py migrate


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории услуг')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории услуг'
        verbose_name_plural = 'Категории услуг'
'''
    Для поиска:
    test in terminal:
    python manage.py shell
    from avto_tochka.models import *
    Service.objects.filter(content__icontains='авто', title__icontains='авто')  # И
    # sqlite не работает с учетом регистр
    from django.db.models import Q
    Service.objects.filter(Q(content__icontains='авто') | Q(title__icontains='авто'))  # или
    Service.objects.filter(Q(content__icontains='авто') & Q(title__icontains='авто'))  # И
    Service.objects.filter(~Q(content__icontains='авто') | Q(title__icontains='авто'))  # не включай "авто" или включай "авто"
    
    выбирать только необходимые поля:
    Service.objects.values('title', 'cat__name').get(pk=1)
'''

"""
    Запись в базу данных:
    В терминале
    python manage.py shell / exit()
    from avto_tochka.models import Service 
    Service(title='Сход Развал', price=800, content="Для легковых")
    Получаем результат: <Service: Service object (None)>  (None) = id записи
    (models является линивыми)
    s1 = _  # (s1 = Service(title='Сход Развал', price=800, content="Для легковых"))
    s1.save()
    запись создана
    s1.id 
    Получаем результат: 1 (id = 1)
    s1.title
    Получаем результат: 'Сход_Развал'
    s1.pk
    Получаем результат: 1 (pk = id = 1)
    
    s2 = Service()
    s2.title = 'Замена тяги'
    s2.price = 500
    s2.content="Замена одной тяги на легковых машин"
    s2.save()
    Вторая запись создана
    
    s3 =  Service.objects.create(title='Замена шаровой', price=700, content="Замена одной шаровой для легковых")
    третья запись создана без s3.save()
    
    Service.objects.create(title='Замена наконечника', price=400, content="Замена одного наконечника для легковых")
    
    импортируем запросы БД
    from django.db import connection
    connection.queries
    
    Вызываем все объекты
    Service.objects.all() 
    
    s = _
    s[0] 
    'Сход_Развал'
    s[0].price 
    800
    
    Лучше использовать 
    Service.objects.filter(title='Замена наконечника')
    <QuerySet [<Service: Замена наконечника>]>
    Service.objects.filter(pk=1)
    <QuerySet [<Service: Сход_Развал>]>
    
    Выбрать запись >=
    Service.objects.filter(pk__gte=1)
    <QuerySet [<Service: Сход_Развал>, <Service: Замена тяги>, <Service: Замена шаровой>, <Service: Замена наконечника>]>

    Выбрать запись <=
    Service.objects.filter(pk__lte=3)
    <QuerySet [<Service: Сход_Развал>, <Service: Замена тяги>]>
    
    Запись не содержит:
    Service.objects.exclude(title='Замена наконечника')
    
    Метод get выберет только 1 запись
    Service.objects.get(pk__gte=1)
    
    Больше или равно 1 филтр по 'title'
    Service.objects.filter(pk__gte=1).order_by('title')
    
    Филтр по 'title'
    Service.objects.order_by('title')
    
    Обратный филтр по 'title'
    Service.objects.order_by('-title')
    
    Менять запись
    s1 = Service.objects.get(pk=1) 
    s1.price = 1000
    s1.save()
    
    Удаление
    sd = Service.objects.filter(pk__gte=3)
    sd.delete()
"""


class Comments(models.Model):
    """ Коммнетарии """
    class Meta():
        db_table = "comments"
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Комментарий к услуге',
                             related_name='comments_service')
    text = models.TextField("Текс комментария", max_length=500)
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name='Разрещение на публикацию')


