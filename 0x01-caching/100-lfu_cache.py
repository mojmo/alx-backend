#!/usr/bin/python3

"""
A caching system that implements the Least Frequently Used
(LFU) algorithm.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system that implements the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.freq = {}  # store the frequency of each key
        self.usage = {}  # store the usage time of each key
        self.time = 0  # store the current time

    def put(self, key, item):
        """
        Assigns the item value for the key in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds its maximum size, discards the least
        frequently used item.
        If there is a tie, discards the least recently used item among them.

        Args:
            key (str): the key of the item.
            item (any): the item to be stored.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists,
            # update the item and increment its frequency
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage[key] = self.time
            self.time += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, find the least frequently used
                # key to discard
                lfu_keys = [k for k, v in self.freq.items()
                            if v == min(self.freq.values())]

                if len(lfu_keys) == 1:
                    lfu_key = lfu_keys[0]
                else:
                    # If there's a tie, find the least recently used
                    # key among them
                    lfu_key = min(lfu_keys, key=lambda k: self.usage[k])
                print("DISCARD:", lfu_key)
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                del self.usage[lfu_key]

            # Add the new key and item to the cache
            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage[key] = self.time
            self.time += 1

    def get(self, key):
        """
        Retrieves the item value linked to the key from the cache.
        Updates the frequency and usage time of the key.

        Args:
            key (str): the key of the item to be retrieved.

        Returns:
            any: the item value linked to the key,
            or None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.usage[key] = self.time
        self.time += 1
        return self.cache_data[key]
