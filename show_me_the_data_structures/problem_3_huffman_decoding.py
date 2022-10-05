import sys
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.frequency = None
        self.left = None
        self.right = None

# Heap class influenced by class from next module
class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        self._up_heapify()

        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break
    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

# From Python heapq documentation
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

test = 'AAAAABBBCCCC'

def get_frequency(string_to_encode):
    frequency_map = {}
    for letter in string_to_encode:
        if letter not in frequency_map:
            frequency_map[letter] = 1
        else:
            frequency_map[letter] += 1
    return frequency_map

def create_priority_queue(frequency_map):
    frequency_list = []
    for letter, frequency in frequency_map.items():
        heapq.heappush(frequency_list, (frequency, letter))
        # node = Node(letter)
        # node.frequency = frequency
        # frequency_list.append(node)
    return frequency_list

def huffman_encoding(data):
    frequency_map = get_frequency(data)
    priority_queue = create_priority_queue(frequency_map)
    first_min_element = heapq.heappop(priority_queue)
    second_min_element = heapq.heappop(priority_queue)
    merge = heapq.merge(first_min_element, second_min_element)
    print(merge)
    pass

huffman_encoding(test)

def huffman_decoding(data,tree):
    pass

# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3