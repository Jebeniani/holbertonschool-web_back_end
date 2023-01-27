#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize cache attributes"""
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.recent_keys.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]
        self.cache_data[key] = item
        self.recent_keys.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.recent_keys.remove(key)
        self.recent_keys.append(key)
        return self.cache_data[key]
