#!/usr/bin/env python3
"""caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
