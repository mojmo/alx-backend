#!/usr/bin/python3

"""A caching system that implements the Most Recently Used (MRU) algorithm."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that implements the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """
        Initializes an empty cache with an MRU eviction strategy.
        """
        super().__init__()
        self.cache_order = []  # Track insertion order for MRU eviction

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following MRU eviction.

        Args:
            key (str): The key to associate with the item.
            item (object): The data to store in the cache.
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move accessed key to the end of the order list (MRU)
            self.cache_order.remove(key)
            self.cache_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # MRU eviction: remove most recently used entry (last element)
                discarded_key = self.cache_order.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_order.append(key)  # Update insertion order

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with a key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            object: The value associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        # Move accessed key to the end of the order list (MRU)
        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data[key]
