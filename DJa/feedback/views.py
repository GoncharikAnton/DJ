from django.shortcuts import render, redirect
from django.views import View

from .forms import FeedbackForm


class FeedbackPost(View):
    """Feedback view"""

    def post(self, request, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('post_slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)

