#!/usr/bin/env python3
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """a cache that uses Redis as the storage backend"""

    def __init__(self):
        """Initializes a new instance of the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in the Redis database
        and returns a randomly generated key for the data."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
