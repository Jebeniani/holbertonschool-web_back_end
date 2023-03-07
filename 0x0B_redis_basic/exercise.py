#!/usr/bin/env python3
from uuid import uuid4
import redis
import functools
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            bytes, str, int, float, None]:
        """
        Retrieves the data associated with the given key from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[bytes, str, None]:
        """
        Retrieves the data associated with the given key
        from Redis and attempts to convert it to a string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[bytes, int, None]:
        """
        Retrieves the data associated with the given key
        from Redis and attempts to convert it to an integer
        """
        return self.get(key, fn=lambda d: int(d))

    def count_calls(func: Callable) -> Callable:
        """Decorator that counts the number of times a method is called
        and stores the count in Redis"""
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = func.__qualname__
            self._redis.incr(key)
            return func(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data in Redis and return the key used to store it"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
