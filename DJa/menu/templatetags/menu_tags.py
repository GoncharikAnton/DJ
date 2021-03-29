from django import template

from ..models import MenuItem

register = template.Library()


def get_menu_item(menu):
    """QuerySet menu item"""
    return MenuItem.objects.filter(
        menu__name=menu,
        menu__published=True,
        published=True
    )


@register.inclusion_tag('base/tags/menu/menu_item_tag.html', takes_context=True)
def menu_item(context, menu, template='base/tags/menu/menu_item_tag.html'):
    """Menu output into template"""
    return {
        'template': template,
        'items': get_menu_item(menu)
    }


@register.simple_tag(takes_context=True)
def for_menu_item(context, menu):
    """Menu output without template"""
    return get_menu_item(menu)
