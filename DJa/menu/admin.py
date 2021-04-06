from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *
# from .forms import MenuItemAdminForm


# admin.site.register(Menu)
# admin.site.register(MenuItem)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Menu"""
    list_display = ('name', 'status', 'published')
    list_filter = ('published', )
    # actions = ['unpublish', 'publish']


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Menu items"""
    # form = MenuItemAdminForm
    list_display = ('id', 'title', 'name', 'parent', 'menu', 'sort', 'published')
    list_filter = ('menu', 'parent', 'published')
    search_fields = ('name', 'parent__name', 'menu__name')
    save_as = True
    list_editable = ('sort', )
    mptt_level_indent = 20
    # actions = ['unpublish', 'publish']