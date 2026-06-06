# middleware.py
from .models import SiteVisit
from django.db.utils import OperationalError

class CountVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_key = 'has_visited'
        try:
            if not request.session.get(session_key, False):
                visit, created = SiteVisit.objects.get_or_create(pk=1)
                visit.total_visits += 1
                visit.save()
                request.session[session_key] = True
        except OperationalError:
            pass

        return self.get_response(request)


# middleware.py
from django.utils.timezone import now
from django.core.cache import cache
from datetime import timedelta

class AnonymousUserTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        now_time = now().timestamp()
        cache.set(f"online:{session_key}", now_time, timeout=300)  # 5 دقیقه

        return self.get_response(request)
