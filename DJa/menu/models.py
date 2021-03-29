from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel



class Menu(models.Model):
    """Model of menu"""

    name = models.CharField('Название', max_length=300)
    is_auth = models.BooleanField('Для зарегистрированных', default=False)
    published = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(MPTTModel):
    """Model of menu points"""

    name = models.CharField('Название пункта меню на латинице', max_length=300)
    title = models.CharField('Название пункта меню на русском', max_length=300)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительский пункт',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name='Меню', on_delete=models.CASCADE, related_name='menu')
    is_auth = models.BooleanField('Для зарегистрированных', default=False)
    anchor = models.CharField('Якорь', max_length=300, null=True, blank=True)
    url = models.URLField('Ссылка на внешний ресурс', max_length=500, null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Ссылка на',
        # limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(verbose_name='id записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    published = models.BooleanField('Отображать?', default=True)
    sort = models.PositiveIntegerField('Порядок', default=0)

    def get_anchor(self):
        if self.anchor:
            return '{}/#{}'.format(Site.objects.get_current().domain, self.anchor)
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_discription = 'id'

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    class MPPTMeta:
        order_insertion_by = ('sort',)
