"""from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .forms import SignupForm, OTPForm
import random
from .models import CustomUser

User = get_user_model()


def generate_otp():
    return str(random.randint(100000, 999999))


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Check if a verified user with this email/username already exists
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(email=email, email_verified=True).exists():
                form.add_error(
                    'email', 'Email already registered and verified.')
            elif CustomUser.objects.filter(username=username, email_verified=True).exists():
                form.add_error('username', 'Username already taken.')
            else:
                otp = generate_otp()

                # ✅ Temporarily store data in session
                request.session['temp_user'] = {
                    'username': form.cleaned_data['username'],
                    'email': form.cleaned_data['email'],
                    'password': form.cleaned_data['password1'],
                    'otp': otp
                }

                # Send OTP
                send_mail(
                    'Your OTP for Email Verification',
                    f'Your OTP is: {otp}',
                    'your_email@gmail.com',
                    [form.cleaned_data['email']],
                    fail_silently=False
                )
                return redirect('verify_otp')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def verify_otp_view(request):
    temp_user = request.session.get('temp_user')

    if not temp_user:
        return redirect('signup')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            if entered_otp == temp_user['otp']:
                # Create and save user
                user = CustomUser.objects.create_user(
                    username=temp_user['username'],
                    email=temp_user['email'],
                    password=temp_user['password'],
                    is_active=True,
                    email_verified=True
                )
                login(request, user)

                # ✅ Use .pop() with default to avoid KeyError
                request.session.pop('temp_user', None)

                return redirect('home')
            else:
                form.add_error('otp', 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()

    return render(request, 'accounts/verify_otp.html', {'form': form})"""
