class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    first_node = llist_1.head
    second_node = llist_2.head
    union_list = []
    while first_node:
        if first_node.value in union_list:
            pass 
        else:
            union_list.append(first_node.value)
        first_node = first_node.next
    while second_node:
        if second_node.value in union_list:
            pass 
        else:
            union_list.append(second_node.value)
        second_node = second_node.next
    return union_list

def intersection(llist_1, llist_2):
    llist_1_array = []
    intersection_array = []
    node = llist_1.head
    node_two = llist_2.head
    if node is None or node_two is None:
        return []
    # Create an array from llist_1
    while node:
        llist_1_array.append(node.value)
        node = node.next
    # Iterate through llist_2, comparing values to llist_1 array
    while node_two:
        if node_two.value in llist_1_array:
            if node_two.value not in intersection_array:
                intersection_array.append(node_two.value)
        node_two = node_two.next
    return intersection_array


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


assert union(linked_list_1,linked_list_2) == [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
assert intersection(linked_list_1,linked_list_2) == [6, 4, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

assert union(linked_list_3,linked_list_4) == [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
assert intersection(linked_list_3,linked_list_4) == []

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1 -- One null linked list

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

assert union(linked_list_5,linked_list_6) == [1,2]
assert intersection (linked_list_5,linked_list_6) == []

# Test Case 2 - One empty array with one array that contains a zero

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [0]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

assert union(linked_list_7,linked_list_8) == [0]
assert intersection(linked_list_7,linked_list_8) == []

# Test Case 3 - Empty arrays

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

assert union(linked_list_9,linked_list_10) == []
assert intersection(linked_list_9,linked_list_10) == []