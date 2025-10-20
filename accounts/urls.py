"""from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, verify_otp_view

urlpatterns = [
    # Signup & OTP
    path('signup/', signup_view, name='signup'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),

    # Login
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        # ✅ Important: show login page even if logged in
        redirect_authenticated_user=False,
    ), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]"""
