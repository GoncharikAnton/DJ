from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        page_context = {'categories': category_list, 'post_list': post_list}
        return render(request, 'blog/post_list.html', context=page_context)


class PostView(View):
    """Post page"""

    def get(self, request, category, post_slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=post_slug)
        page_context = {'categories': category_list, 'post': post}
        return render(request, post.template, context=page_context)


class CategoryView(View):
    """Category page"""

    def get(self, request, category_slug=None, tag_slug=None):
        post_list = []
        if category_slug is not None:
            post_list = Post.objects.filter(
                category__slug=category_slug,
                category__published=True,
                published=True
            )
        elif tag_slug is not None:
            post_list = Post.objects.filter(tags__slug=tag_slug, published=True)
        category_list = Category.objects.all()
        if post_list.exists():
            template = post_list.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'categories': category_list, 'post_list': post_list})
