#!/usr/bin/env python3

"""
This module defines the `BasicCache` class, which offers a straightforward
in-memory cache implementation inheriting from the abstract `BaseCaching` class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache implementation.
    """

    def put(self, key, item):
        """
        Puts an item in the cache.

        Args:
            key (str): The key to associate with the item.
            item (object): The data to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            object: The value associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None)
