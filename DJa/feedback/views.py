from django.shortcuts import render, redirect
from django.views import View

from .forms import FeedbackForm


class FeedbackPost(View):
    """Feedback view"""

    def post(self, request, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # form = form.save(commit=False)
            # form.post_id = request.POST.get('post')
            # form.author = request.user
            form.save()
        return redirect(request.path)

