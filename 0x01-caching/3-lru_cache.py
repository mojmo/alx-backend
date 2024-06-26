#!/usr/bin/python3

"""A caching system that implements the Least Recently Used (LRU) algorithm."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system that implements the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """
        Initializes an empty cache with an LRU eviction strategy.
        """
        super().__init__()
        self.cache_data = {}
        self.cache_order = []  # Track access order for LRU eviction

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following LRU eviction.

        Args:
            key (str): The key to associate with the item.
            item (object): The data to store in the cache.
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move accessed key to the front of the order list (LRU)
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU eviction: remove least recently used entry
                discarded_key = self.cache_order.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_order.append(key)  # Update access order

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            object: The value associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        # Move accessed key to the front of the order list (LRU)
        self.cache_order.remove(key)
        self.cache_order.insert(0, key)
        return self.cache_data[key]
