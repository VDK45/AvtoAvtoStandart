from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)  # Пустое = False
    # Нужно установить pillow

    # Нужно добавить в seting.py
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # MEDIA_URL = '/media/'

    # Нужно добавить в avtosite\url.py
    # if settings.DEBUG:  # import from avtosite
    #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  # Загрузить в "photos/%Y/%m/%d/"
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# in terminal: python manage.py makemigrations
# Show sql command: python manage.py sqlmigrate avto_tochka 0001
# Create table: python manage.py migrate
