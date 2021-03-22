from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from .forms import CommentForm


class PostListView(View):
    """Category page"""

    def get_qeryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        category_list = Category.objects.filter(published=True)
        if category_slug is not None:
            post_list = self.get_qeryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            post_list = self.get_qeryset().filter(tags__slug=tag_slug, tags__published=True)
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
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get('post_slug'))
        form = CommentForm()
        page_context = {'categories': category_list, 'post': post, 'form': form}
        return render(request, post.template, context=page_context)


class CreateCommentView(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)

            form.post_id = pk
            form.author = request.user
            form.save()
        return HttpResponse(status=201)
