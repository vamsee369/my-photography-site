from .models import ActiveSession
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS = [
    '/accounts/login/',
    '/accounts/signup/',
    '/accounts/verify-otp/',
    '/admin/login/',
]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if not request.user.is_authenticated and not any(path.startswith(url) for url in EXEMPT_URLS):
            return redirect(reverse('login'))

        return self.get_response(request)


class UpdateLastSeenMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        ActiveSession.objects.update_or_create(
            session_key=session_key,
            defaults={'last_seen': timezone.now()}
        )
        return None
