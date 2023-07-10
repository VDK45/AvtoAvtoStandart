from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddServiceForm_test(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание услуги", required=False)
    price = forms.IntegerField(label='Цена')
    photo = forms.ImageField(label='Цена', required=False)
    is_published = forms.BooleanField(label="Публикация", initial=True, required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории услуг", empty_label="Категория не выбрана")


class AddServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'price', 'cat', 'is_published']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # Своя проверка
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

