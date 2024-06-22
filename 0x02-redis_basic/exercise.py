#!/usr/bin/env python3
"""Writing strings 
"""
import uuid
import redis


class Cache():
    """ class cache
    """
    def __init__(self, redis):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
