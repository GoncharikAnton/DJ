from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        page_context = {'categories': category_list, 'post_list': post_list}
        return render(request, 'blog/home.html', context=page_context)


class CategoryView(View):
    """Category page"""

    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})

#
# class PostView(View):
#     """Post page"""
#
#     def get(self, request, post_title):
#         category_list = Category.objects.all()
#         post = Post.objects.get(slug=post_title)
#         page_context = {'categories': category_list, 'post': post}
#         return render(request, 'blog/post_list.html', context=page_context)
