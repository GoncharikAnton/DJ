from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Page(models.Model):
    """Model of pages"""

    title = models.CharField('Название', max_length=800)
    text = models.CharField('Содержание', max_length=8000)
    active = models.BooleanField('Вкл\Выкл', default=True)
    template = models.CharField('Шаблон', default='page/index.html')
    slug = models.SlugField('url', max_length=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
