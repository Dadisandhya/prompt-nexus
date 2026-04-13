import redis

try:
    # r = redis.Redis(host='localhost', port=6379, db=0)
    r = redis.Redis(host='redis', port=6379, db=0)
    r.ping()
except:
    r = None   # safe fallback

def increment_view(prompt_id):
    if r:
        return r.incr(f"prompt:{prompt_id}:views")
    return 0

def get_views(prompt_id):
    if r:
        value = r.get(f"prompt:{prompt_id}:views")
        return int(value) if value else 0
    return 0