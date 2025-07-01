from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photography/', views.photography, name='photography'),
    path('travel/', views.travel, name='travel'),
    path('blog/', views.blog, name='blog'),
]
