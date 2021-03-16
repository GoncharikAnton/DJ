from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    '''Class of comment form'''

    class Meta:
        model = Comment
        fields = ('text', )