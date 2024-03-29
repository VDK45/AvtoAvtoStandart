from django import template
from avto_tochka.models import *

register = template.Library()


@register.simple_tag(name='getcat_tag')
def get_categories(filter):
        return Category.objects.filter(pk=filter)[0]


@register.simple_tag(name='getbrand_tag')
def get_brands(filter):
        return Brand.objects.filter(pk=filter)[0]


@register.simple_tag(name='getcats_tag')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('avto_tochka/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('avto_tochka/list_services.html')
def show_services(cat_selected):
    if cat_selected == 0:
        services = Service.objects.filter(is_published=True)
    else:
        services = Service.objects.filter(cat=cat_selected, is_published=True)

    return {"services": services, "cat_selected": cat_selected}
