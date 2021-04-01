from django import template
from django.shortcuts import redirect

from ..models import FeedBack
from ..forms import FeedbackForm
from ..views import FeedbackPost

register = template.Library()


@register.simple_tag(takes_context=False)
def post(self, request, **kwargs):
    return FeedbackPost
# def post(self, request, **kwargs):
#     """Post feedback"""
#     form = FeedbackForm(request.POST)
#     if form.is_valid():
#         # form = form.save(commit=False)
#         # form.author = request.user
#         form.save()
#     return redirect(request.path)

# @register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
# def feedback_post(context, template='base/tags/feedback/feedback_tag.html'):
#     """template tag for feedback post"""
#     feedback_pos = post(context)
#     return {'template': template, 'feedback_pos': feedback_pos}
#
