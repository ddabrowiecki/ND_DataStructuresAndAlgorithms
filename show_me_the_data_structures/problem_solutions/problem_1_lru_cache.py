class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return

        if self.head.value == value:
            self.head = self.head.next

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.lru_linked_list = LinkedList()
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if hasattr(self, str(key)):
            value = getattr(self, str(key))
            if self.lru_linked_list.head == str(key):
                self.lru_linked_list.head = self.lru_linked_list.head.next
            self.lru_linked_list.append(str(key))
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.size >= self.capacity:
            delattr(self, str(self.lru_linked_list.head.value))
        else:
            setattr(self, str(key), value)
            self.size += 1
            self.lru_linked_list.append(str(key))

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2

our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)     # returns -1 because the cache reached its capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
test_case_1_cache = LRU_Cache(5)

test_case_1_cache.set(1, 1)
test_case_1_cache.set(2, 2)
test_case_1_cache.set(3, 3)
test_case_1_cache.set(4, 4)

test_case_1_cache.get(1)
test_case_1_cache.get(2)
test_case_1_cache.get(3)

test_case_1_cache.set(5,5)
test_case_1_cache.get(2)
test_case_1_cache.get(3)
test_case_1_cache.set(6,6)

assert test_case_1_cache.get(4) == -1

# Test Case 2

test_case_2_cache = LRU_Cache(3)

test_case_2_cache.set(2, 2)
test_case_2_cache.set(3, None)
test_case_2_cache.set(4, 4)

test_case_2_cache.get(2)
test_case_2_cache.set(5, 4)

assert test_case_2_cache.get(3) == -1

# Test Case 3
test_case_3_cache = LRU_Cache(2)

test_case_3_cache.set(2, 2)
test_case_3_cache.set(3, 3)
test_case_3_cache.set(4, 4)

assert test_case_3_cache.get(2) == -1