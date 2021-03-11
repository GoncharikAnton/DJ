from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *



class PostListView(View):
    """Category page"""

    def get_qeryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        category_list = Category.objects.all()
        if category_slug is not None:
            post_list = self.get_qeryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            post_list = self.get_qeryset().filter(tags__slug=tag_slug)
        else:
            post_list = self.get_qeryset()
        if post_list.exists():
            template = post_list.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'categories': category_list, 'post_list': post_list})


class PostView(View):
    """Post page"""

    def get(self, request, **kwargs):
        category_list = Category.objects.all()
        post = get_object_or_404(Post, slug=kwargs.get('post_slug'))
        page_context = {'categories': category_list, 'post': post}
        return render(request, post.template, context=page_context)
