#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching System"""

    def __init__(self) -> None:
        """Initialize cache attributes"""
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last}")
                del (self.cache_data[self.last])
            self.last = key

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is not None:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
