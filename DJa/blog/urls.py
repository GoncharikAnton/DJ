from django.urls import path

from . import views


urlpatterns = [
    path('<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    # path('<slug:post_title>/', views.PostView.as_view(), name='post'),
    path('', views.HomeView.as_view()),
]
