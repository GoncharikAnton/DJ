from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Модель категорий постов"""

    name = models.CharField('Категории', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)
    description = models.TextField('Описание категории', max_length=1000, default='', blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField('Шаблон', max_length=500, default='blog/post_list.html')
    published = models.BooleanField('Отображать?', default=True)
    paginated = models.PositiveIntegerField('Кол-во новостей на страние', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

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
        verbose_name='Автор',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField('Название', max_length=250)
    subtitle = models.CharField('Подзаголовок', max_length=500, blank=True, null=True)
    slug = models.SlugField('url', max_length=250, unique=True)
    mini_text = models.TextField('Краткое описание', max_length=400)
    text = models.TextField('Описание', max_length=2000000)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    edit_date = models.DateTimeField(
        'Дата изменения',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField('Главная фотография', upload_to='post/', blank=True, null=True)
    template = models.CharField('Шаблон', max_length=500, default='news/post_detail.html')
    published = models.BooleanField('Отображать?', default=True)
    viewed = models.IntegerField('Просмотрено', default=0)
    status = models.BooleanField('Для зарегестриованных', default=False)
    sort = models.PositiveIntegerField('Порядок', default=0)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'post': self.slug})

    def __str__(self):
        return f'{self.title} {self.mini_text} {self.text} {self.created_date}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    """Comment's model"""

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)
    text = models.TextField('Описание', max_length=750)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    moderation = models.BooleanField('Модерация пройдена', blank=False)


    def __str__(self):
        return f'{self.text} {self.created_date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
