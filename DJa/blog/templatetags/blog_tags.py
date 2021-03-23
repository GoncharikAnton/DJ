from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def total_categories():
    category_list = Category.objects.filter(published=True, )
    return category_list
