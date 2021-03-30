from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from .forms import CommentForm


class PostListView(View):
    """Category page"""

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        # category_list = Category.objects.filter(published=True)
        if category_slug is not None:
            post_list = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            post_list = self.get_queryset().filter(tags__slug=tag_slug, tags__published=True)
        else:
            post_list = self.get_queryset()
        if post_list.exists():
            template = post_list.first().get_category_template()
        else:
            raise Http404()
            # template = 'blog/post_list.html'
        return render(request, template, {'post_list': post_list})


class PostView(View):
    """Post page"""

    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get('post_slug'))
        form = CommentForm()
        page_context = {'categories': category_list, 'post': post, 'form': form}
        return render(request, post.template, context=page_context)

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('post_slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)
