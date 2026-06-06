# utils.py
from django.core.cache import cache
from django.utils.timezone import now
from datetime import timedelta

def get_online_anonymous_count():
    count = 0
    now_ts = now().timestamp()
    try:
        keys = cache.iter_keys("online:*")
    except (AttributeError, NotImplementedError):
        return 0

    for key in keys:
        last_seen_ts = cache.get(key)
        if last_seen_ts and now_ts - last_seen_ts < 60:
            count += 1

    return count
