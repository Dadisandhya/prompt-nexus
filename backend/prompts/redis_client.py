import redis
import os

try:
    redis_url = os.environ.get("REDIS_URL")

    if redis_url:
        r = redis.Redis.from_url(redis_url)
    else:
        r = redis.Redis(host='localhost', port=6379, db=0)

    r.ping()
except:
    r = None


def increment_view(prompt_id):
    if r:
        return r.incr(f"prompt:{prompt_id}:views")
    return 0


def get_views(prompt_id):
    if r:
        value = r.get(f"prompt:{prompt_id}:views")
        return int(value) if value else 0
    return 0
