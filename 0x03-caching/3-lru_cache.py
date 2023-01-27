#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """Initialize cache attributes"""
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.recent_keys.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]
        self.cache_data[key] = item
        self.recent_keys.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.recent_keys.remove(key)
        self.recent_keys.append(key)
        return self.cache_data[key]
