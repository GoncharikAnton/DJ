from django.urls import path

from . import get_page


urlpatterns = [
    path('<path:url>', get_page, name='page'),
]

