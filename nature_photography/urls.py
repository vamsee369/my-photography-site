from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photography/', views.photography, name='photography'),
    path('travel/', views.travel, name='travel'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('', views.home, name='home'),

]
