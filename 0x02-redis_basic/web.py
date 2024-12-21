#!/usr/bin/env python3
"""
web.py
"""
import requests
import redis
from functools import wraps

redis_client = redis.Redis()

def count_access(func):
    """Decorator to count the number of accesses to a URL."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0]  # Assuming the first argument is the URL
        redis_client.incr(f"access_count:{url}")
        return func(*args, **kwargs)
    return wrapper

def cache_page(expiration_time=10):
    """Decorator to cache the page content with an expiration time."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            cached_content = redis_client.get(url)
            if cached_content:
                return cached_content.decode('utf-8')
            content = func(*args, **kwargs)
            redis_client.setex(url, expiration_time, content.encode('utf-8'))
            return content
        return wrapper
    return decorator

@cache_page(expiration_time=10)
@count_access
def get_page(url: str) -> str:
    """Obtain the HTML content of a given URL."""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://google.com"
    print(get_page(url))
    print(get_page(url))
    print(redis_client.get(f"access_count:{url}"))

