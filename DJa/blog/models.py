from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Модель категорий постов"""

    name = models.CharField('Категории', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Tag's model"""

    name = models.CharField('Тег', max_length=60)
    slug = models.SlugField('url', max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    """Post's model"""

    author = models.ForeignKey(
        User,
        verbose_name='Автора',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField('Нахзвание', max_length=250)
    mini_text = models.TextField('Краткое описание', max_length=400)
    text = models.TextField('Описание', max_length=2000000)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    slug = models.SlugField('url', max_length=250, unique=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)

    def __str__(self):
        return f'{self.title} {self.mini_text} {self.text} {self.created_date}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    """Comment's model"""

    text = models.TextField('Описание', max_length=750)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    moderation = models.BooleanField('Модерация пройдена', blank=False)
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.text} {self.created_date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
