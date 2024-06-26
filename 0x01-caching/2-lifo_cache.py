#!/usr/bin/python3

"""A caching system that implements the Last-In-First-Out (LIFO) algorithm."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    """
    A caching system that implements the Last-In-First-Out (LIFO) algorithm.
    """

    def __init__(self):
        """Initializes an empty cache with a LIFO eviction strategy."""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following LIFO eviction.

        Args:
            key (str): The key to associate with the item.
            item (object): The data to store in the cache.
        """

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """
        Gets an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            object: The value associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None)
