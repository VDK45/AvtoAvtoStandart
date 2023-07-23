from django.db.models import Count

from .models import *

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить услугу", 'url_name': 'add_page'},
        ]


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('service'))

        user_menu = menu.copy()
        if not self.request.user.is_superuser:
            user_menu.pop(2)

        context['menu'] = user_menu

        context['cats'] = cats  # tag для html
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
