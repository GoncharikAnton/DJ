from django.urls import path

from . import views


urlpatterns = [
    path('tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('<slug:category>/<slug:post_slug>', views.PostView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
]

