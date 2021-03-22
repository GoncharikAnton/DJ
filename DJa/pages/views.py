from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *

class PageView(View):
    """Pages view"""

    # def get(self, request, **kwargs):
    #     category_list = Category.objects.filter(published=True)
    #     post = get_object_or_404(Post, slug=kwargs.get('post_slug'))
    #     form = CommentForm()
    #     page_context = {'categories': category_list, 'post': post, 'form': form}
    #     return render(request, post.template, context=page_context)
