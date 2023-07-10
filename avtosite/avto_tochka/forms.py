from django import forms
from .models import *


class AddServiceForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание услуги", required=False)
    price = forms.IntegerField(label='Цена')
    photo = forms.ImageField(label='Цена', required=False)
    is_published = forms.BooleanField(label="Публикация", initial=True, required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории услуг", empty_label="Категория не выбрана")

