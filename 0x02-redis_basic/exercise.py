#!/usr/bin/env python3
"""Writing strings 
"""
import uuid
import redis
from typing import Union, Callable, Optional


class Cache():
    """ class cache
    """
    def __init__(self, redis):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(name=key, value=data)
        return key
