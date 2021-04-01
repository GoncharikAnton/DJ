from django.urls import path

from .views import FeedbackPost


urlpatterns = [
    path('<path:url>', FeedbackPost, name='feedback'),

]
