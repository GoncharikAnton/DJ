from django import forms

from .models import FeedBack


class FeedbackForm(forms.ModelForm):
    '''Class of feedback form'''

    class Meta:
        model = FeedBack
        fields = ('user_name', 'email', 'text')
