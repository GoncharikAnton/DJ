from django import forms
from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# admin.site.register(Pages)

class ActionPublish(admin.ModelAdmin):
    """Action for publish and unpublish"""

    def unpublish(self, request, queryset):
        """Unpublish"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = '1 story was'
        else:
            message_bit = '%s stories were' % rows_updated
        self.message_user(request, '%s successefully marked as published.' % message_bit)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permission = ('change',)

    def publish(self, request, queryset):
        """Publish"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = '1 story was'
        else:
            message_bit = '%s stories were' % rows_updated
        self.message_user(request, '%s successefully marked as published.' % message_bit)

    publish.short_description = 'Опубликовать'
    publish.allowed_permission = ('change',)


class PagesAdminForm(forms.ModelForm):
    """Widget of ckeditor editor"""
    text = forms.CharField(required=False, label='Контент страницы', widget=CKEditorUploadingWidget())

    class Meta:
        model = Pages
        fields = '__all__'


@admin.register(Pages)
class PagesAdmin(ActionPublish):
    """Static pages"""
    list_display = ('title', 'published', 'id')
    list_editable = ('published',)
    list_filter = ('published', 'template')
    search_field = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    form = PagesAdminForm
    actions = ['unpublish', 'publish']
    save_on_top = True
    # readonly_fields = ('get_slug_url',)
