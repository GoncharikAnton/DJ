from django.urls import path

from . import views


urlpatterns = [
    path('', views.PageView.as_view(), name='page_list'),
    path('<slug:page_slug>/', views.PageDetailView.as_view(), name='page_detail'),


]

