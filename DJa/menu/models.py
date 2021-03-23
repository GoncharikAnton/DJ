from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class Menu(models.Model):
    """Model of menu"""

    name = models.CharField('Название', max_length=300)
    is_auth = models.BooleanField('Для зарегистрированных', default=False)
    active = models.BooleanField('Активно вкл/выкл', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuPoint(MPTTModel):
    """Model of menu points"""

    name = models.CharField('Название на латинице', max_length=300)
    title = models.CharField('Название на русском', max_length=300)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='menu'
    )
    status = models.BooleanField('Вкл/выкл', default=True)
    is_auth = models.BooleanField('Для зарегистрированных', default=False)
    anchor = models.CharField('Якорь', max_length=300)
    url = models.URLField('Ссылка на внешний ресурс', max_length=500)
    active = models.BooleanField('Активно вкл/выкл', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
