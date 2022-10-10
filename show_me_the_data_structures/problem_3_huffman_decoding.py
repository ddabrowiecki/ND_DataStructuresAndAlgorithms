import code
import sys
import heapq

class Node:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return (self.frequency < other.frequency)

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
        node = Node(letter, frequency)
        heapq.heappush(frequency_list, node)
    return frequency_list

def traverse_heap(table, node, code):
    if not node.left and not node.right:
        table[node.value] = code
        return table
    if node.left:
        traverse_heap(table, node.left, code + "0")
    if node.right:
        traverse_heap(table, node.right, code + "1")
    return table

# Received helpful advice from these posts https://knowledge.udacity.com/questions/362115 and
# https://knowledge.udacity.com/questions/471504
def huffman_encoding(data):
    if len(data) == 0:
        return ("", None)
    frequency_map = get_frequency(data)
    priority_queue = create_priority_queue(frequency_map)
    # Create Huffman tree
    while len(priority_queue) > 1:
        first_min_element = heapq.heappop(priority_queue)
        second_min_element = heapq.heappop(priority_queue)
        merged_frequency = first_min_element.frequency + second_min_element.frequency
        node = Node("", merged_frequency)
        node.left = first_min_element
        node.right = second_min_element
        heapq.heappush(priority_queue, node)
    tree = priority_queue[0]
    code_table = traverse_heap({}, tree, "")
    encoded_data = ''
    for letter in data:
        encoded_data += code_table[letter]
    return encoded_data, tree
            
def huffman_decoding(data, tree):
    if data is None:
        return None
    decoded_string = ""
    current = tree
    for number in data:
        if number == "0":
            current = current.left
        if number == "1":
            current = current.right
        if not current.left and not current.right:
            decoded_string += current.value
            current = tree
    return decoded_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

test_string = "Wow this secret code is really cool"
print ("The size of the data is: {}\n".format(sys.getsizeof(test_string)))
print ("The content of the data is: {}\n".format(test_string))

data, tree = huffman_encoding(test_string)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(data, base=2))))
print ("The content of the encoded data is: {}\n".format(data))

decoded_data = huffman_decoding(data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

assert sys.getsizeof(test_string) == 84
assert sys.getsizeof(int(data, base=2)) == 44
assert sys.getsizeof(decoded_data) == 84
assert test_string == decoded_data

# Test Case 2

test_string_2 = "A"
print ("The size of the data is: {}\n".format(sys.getsizeof(test_string_2)))
print ("The content of the data is: {}\n".format(test_string_2))

data, tree = huffman_encoding(test_string_2)

if data and len(data) > 0:
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(data, base=2))))
    print ("The content of the encoded data is: {}\n".format(data))
else:
    print('Data not encoded')


decoded_data = huffman_decoding(data, tree)
if decoded_data and len(data) > 0:
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

assert len(data) == 0
assert sys.getsizeof(test_string_2) == 50

# Test Case 3

test_string_3 = ""
print ("The size of the data is: {}\n".format(sys.getsizeof(test_string_3)))
print ("The content of the data is: {}\n".format(test_string_3))

data, tree = huffman_encoding(test_string_3)
if data and len(data) > 0:
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(data, base=2))))
    print ("The content of the encoded data is: {}\n".format(data))
else:
    print("Data not encoded")

decoded_data = huffman_decoding(data, tree)
if decoded_data and len(data) > 0:
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

assert len(data) == 0
assert sys.getsizeof(test_string_3) == 49