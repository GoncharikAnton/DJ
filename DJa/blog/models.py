from django.db import models


class Category(models.Model):
    """Модель категорий постов"""

    name = models.CharField('Категории', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Tag's model"""

    name = models.CharField('Тэг', max_length=60)
    slug = models.SlugField('url', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    """Post's model"""

    title = models.CharField('Нахзвание', max_length=250)
    mini_text = models.TextField('Краткое описание', max_length=400)
    text = models.TextField('Описание', max_length=2000)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    slug = models.SlugField('url', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    """Comment's model"""

    text = models.TextField('Описание', max_length=750)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    moderation = models.BooleanField('Модерация пройдена', blank=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
