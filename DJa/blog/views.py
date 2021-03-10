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

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        category_list = Category.objects.all()
        post_list = Post.objects.filter(
            category__slug=category_slug,
            category__published=True,
            published=True
        )

        return render(
            request,
            post_list.first().get_category_template(),
            {
                'categories': category_list,
                'category': category,
                'post_list': post_list
            }
        )

class TagView(View):
    """Tag's page"""

    def get(self, request, tag_slug):
        tag = Tag.objects.get(slug=tag_slug)
        category_list = Category.objects.all()
        post_list = Post.objects.filter(tags__slug=tag_slug, published=True)

        return render(
            request,
            post_list.first().get_category_template(),
            {
                'categories': category_list,
                'tag': tag,
                'post_list': post_list
            }
        )


# class CategoryView(View):
#     """Category page"""
#
#     def get(self, request, category_name, post_slug):
#         category_list = Category.objects.all()
#         if request == post_slug:
#             post_detail = Post.objects.get(slug=post_slug)
#             page_context = {
#                 'categories': category_list,
#                 'post_detail': post_detail
#             }
#             template = post_detail.template
#         else:
#             category = Category.objects.get(slug=category_name)
#             post_list = Post.objects.filter(category=category, published=True)
#             page_context = {
#                 'categories': category_list,
#                 'category': category,
#                 'post_list': post_list,
#             }
#             template = category.template
#
#
#
#
#         return render(request, template, page_context)
