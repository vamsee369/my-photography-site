from .forms import ContactForm
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def photography(request):
    return render(request, 'photography.html')


@login_required(login_url='/accounts/login/')
def travel(request):
    return render(request, 'travel.html')


@login_required(login_url='/accounts/login/')
def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
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
