from django import template
from ..models import Category

register = template.Library()


#s
# @register.simple_tag
# def total_categories():
#     category_list = Category.objects.filter(published=True, )
#     return category_list

def get_categories(context, count, order=None):
    """Take a list of categories"""
    categories = Category.objects.filter(published=True)
    if count is not None:
        categories = categories[:count]
    return categories


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(context, count=None, template='base/tags/blog/categories.html'):
    """template tag for category output"""
    categories = get_categories(context, count)
    return {'template': template, 'category_list': categories}


@register.simple_tag(takes_context=True)
def for_category_list(context, order='-sort', count=None):
    """Output of template-tag without template"""
    return get_categories(context, order, count)
