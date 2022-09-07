class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    
# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    prepend_node = Node(value)
    prepend_node.next = self.head
    self.head = prepend_node

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here 
    if self.head == None:
        self.head = Node(value)
        return
    node = self.head
    while node.next:
        node = node.next
    node.next = Node(value)

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head
    while node.next:
        node = node.next
        if node.value == value:
            return node

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head.value == value:
        self.head = self.head.next
        return
    node = self.head
    while node.next:
        node = node.next
        if node.next.value == value:
            if node.next.next:
                node.next = node.next.next
                return
            else:
                node.next = None

def pop(self):
    """ Return the first node's value and remove it from the list. """
    value = self.head.value
    self.head = self.head.next
    return value

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
    position = 0
    node = self.head
    insert_node = Node(value)
    if pos == 0:
        self.head = insert_node
        self.head.next = node
        return
    
    while node.next:
        if position + 1 == pos:
            insert_node.next = node.next
            node.next = insert_node
            return
        node = node.next
        position += 1
    node.next = insert_node

def size(self):
    """ Return the size or length of the linked list. """
    node = self.head
    length = 1
    while node.next:
        node = node.next
        length += 1
    return length

LinkedList.size = size
LinkedList.insert = insert
LinkedList.pop = pop
LinkedList.remove = remove
LinkedList.search = search
LinkedList.append = append
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"