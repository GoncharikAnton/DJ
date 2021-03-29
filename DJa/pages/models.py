from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, get_script_prefix
from django.utils.encoding import iri_to_uri


class Pages(models.Model):
    """Model of pages"""

    title = models.CharField('Заголовок', max_length=800)
    sub_title = models.CharField('Подзаголовок', max_length=800, blank=True, null=True)
    text = models.CharField('Содержание', max_length=8000)
    edit_date = models.DateTimeField(
        'Дата редактирования',
        blank=True,
        null=True
    )
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)
    published = models.BooleanField('Опубликовать?', default=True)
    # active = models.BooleanField('Активно Вкл\Выкл', default=True)
    template = models.CharField('Шаблон', default='page/index.html', max_length=500)
    slug = models.SlugField('url', max_length=250, unique=True)
    registration_required = models.BooleanField('Требуется регистрация',
                                                default=False,
                                                help_text='Если флажок установлен, то только'
                                                          'зарегестрированные пользователи могут просматривать '
                                                          'страницу. '
                                                )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = '/'
        if not f'{self.slug}'.startswith('/'):
            self.slug = '/' + self.slug
        if not self.slug.endswith('/'):
            self.slug += '/'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + '/page' + self.slug)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
