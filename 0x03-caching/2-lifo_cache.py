#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize cache attributes"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
