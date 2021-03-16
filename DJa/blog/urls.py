from django.urls import path

from . import views


urlpatterns = [
    path('comment/', views.CreateCommentView.as_view(), name='add-comment'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='tag'),
    path('<slug:category>/<slug:post_slug>', views.PostView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', views.PostListView.as_view(), name='category'),
    path('', views.PostListView.as_view()),
]

