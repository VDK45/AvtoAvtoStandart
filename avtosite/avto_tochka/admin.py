from django.contrib import admin

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # Редактруемое поле
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}  # Атоматом создает slug по title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # Запятая обязательная
    prepopulated_fields = {"slug": ('name',)}  # Повторяет поле name


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'status')
    list_display_links = ('user', 'post')
    search_fields = ('text', )
    list_editable = ('status', )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
