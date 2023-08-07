from allauth.socialaccount.models import SocialApp
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # Редактруемое поле
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}  # Атоматом создает slug по title
    fields = ('title', 'slug', 'price', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True  # Панель управления на верху

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # Запятая обязательная
    prepopulated_fields = {"slug": ('name',)}  # Повторяет поле name


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # Запятая обязательная
    prepopulated_fields = {"slug": ('name',)}  # Повторяет поле name


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'created', 'status')
    list_display_links = ('user', 'post', 'created')
    search_fields = ('text', )
    list_editable = ('status', )
    # list_filter = ('user', 'post')
    save_on_top = True  # Панель управления на верху


# django-allauth
class SocialAppAdmin(admin.ModelAdmin):
    model = SocialApp
    menu_icon = 'placeholder'
    add_to_setting_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'provider')
    save_on_top = True


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Brand, BrandsAdmin)

admin.site.site_title = 'Админ-панель сайта Авто стандарт'
admin.site.site_header = 'Админ-панель сайта Авто стандарт'