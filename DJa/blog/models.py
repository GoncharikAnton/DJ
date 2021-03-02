from django.db import models


class Category(models.Model):
    """Модель категорий постов"""

    name = models.CharField('Категории', max_length=100)
    slug = models.SlugField('url', max_length=100)
