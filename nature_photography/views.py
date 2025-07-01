from .models import BlogPost
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def photography(request):
    return render(request, 'photography.html')


def travel(request):
    return render(request, 'travel.html')


def blog(request):
    return render(request, 'blog.html')


def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})
