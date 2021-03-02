from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        return render(request, 'blog/home.html', {'categories': category_list})


class CategoryView(View):
    """Category view"""

    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})
