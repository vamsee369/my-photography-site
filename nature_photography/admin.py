from django.contrib import admin
from .models import BlogPost
from .models import ContactMessage

admin.site.register(BlogPost)
admin.site.register(ContactMessage)
