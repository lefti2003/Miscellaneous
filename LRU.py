# LRU (Least Recently Used)
# A cache implemented using the LRU strategy
# organizes its items in order of use.
# Every time you access an entry, the LRU algorithm
# will move it to the top of the cache.
# This way, the algorithm can quickly identify the entry
# that’s gone unused the longest by looking at the bottom of the list.

from _collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity=5):
        self.bucket_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.bucket_dict:
            return -1
        else:
            self.bucket_dict.move_to_end(key)
            return self.bucket_dict[key]

    def add_to_end(self, key, value):
        self.bucket_dict[key] = value
        self.bucket_dict.move_to_end(key)

    def set(self, key, value):

        if self.capacity == 0:
            print("Length of dictionary is 0 cannot add items")

        elif len(self.bucket_dict) < self.capacity:
            self.add_to_end(key, value)

        else:
            self.bucket_dict.popitem(last=False)
            self.add_to_end(key, value)

# Test 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1

print(our_cache.get(2))
# returns 2
print(our_cache.get(9))

# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity
# and 3 was the least recently used entry

# Test 2
# A cache with 0 capacity
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# Length of dictionary is 0 cannot add items

# Test 3
# A cache with capacity of 1 item
our_cache = LRU_Cache(1)
our_cache.set(1, 1)

print(our_cache.get(1))
# 1
print(our_cache.get(2))
# -1


