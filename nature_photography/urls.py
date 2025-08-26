from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photography/', views.photography, name='photography'),
    path('photos/', views.photo_gallery, name='photo_gallery'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('travel/', views.travel, name='travel'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path("active-users/", views.active_users_api, name="active_users_api"),
]
