from .models import ActiveSession
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import timedelta
from .forms import ContactForm
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib import messages

# from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')


def photography(request):
    return render(request, 'photography.html')


def travel(request):
    return render(request, 'travel.html')


def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, '📩 Your message has been sent successfully!')
            return redirect('contact')  # Optionally show success message
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def photo_gallery(request):
    return render(request, 'photo_gallery.html')


def video_gallery(request):
    return render(request, 'video_gallery.html')


def active_users_api(request):
    now = timezone.now()
    five_minutes_ago = now - timedelta(minutes=5)
    count = ActiveSession.objects.filter(
        last_seen__gte=five_minutes_ago).count()
    return JsonResponse({"active_users": count})
