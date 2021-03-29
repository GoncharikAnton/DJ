from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *


class PageDetailView(View):
    """One Page view"""

    # def get(self, request, **kwargs):
    #     category_list = Category.objects.filter(published=True)
    #     post = get_object_or_404(Post, slug=kwargs.get('post_slug'))
    #     form = CommentForm()
    #     page_context = {'categories': category_list, 'post': post, 'form': form}
    #     return render(request, post.template, context=page_context)

    def get(self, request, page_slug=None):
        page_list = Pages.objects.filter(slug=f'/{page_slug}/')
        page_context = {'page_list': page_list}
        print(request)
        print(page_list)
        print('page-slug', page_slug)
        return render(request, 'page/index.html', context=page_context)

class PageView(View):
    """All pages view"""

    def get(self, request, page_slug=None):
        page_list = Pages.objects.filter(published=True)
        page_context = {'page_list': page_list}
        return render(request, 'page/index.html', context=page_context)
