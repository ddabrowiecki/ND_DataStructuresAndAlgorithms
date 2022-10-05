import sys
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.frequency = None
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return (self.frequency < other.frequency)

test = 'The bird is the word Lets just make very fucking sure that it can handle it'

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
        node = Node(letter)
        node.frequency = frequency
        heapq.heappush(frequency_list, (frequency, node))
    return frequency_list

def traverse(root):
    visit_order = []
    tuple = root
    code = []
    def traverse(tuple, code):
        if tuple:
            if tuple[1].left:
                code.append("0")
            traverse(tuple[1].left, code)
            if tuple[1].right:
                code.append("1")
            visit_order.append(tuple[1].value)
            if not tuple[1].left and not tuple[1].right:
                visit_order.append('blah')
            traverse(tuple[1].right, code)
    code = []
    traverse(tuple, code)
    return ''.join(code)

# Received helpful advice from this post https://knowledge.udacity.com/questions/362115
def huffman_encoding(data):
    frequency_map = get_frequency(data)
    priority_queue = create_priority_queue(frequency_map)

    # Create Huffman tree
    while len(priority_queue) > 1:
        first_min_element = heapq.heappop(priority_queue)
        second_min_element = heapq.heappop(priority_queue)
        merged_frequency = first_min_element[0] + second_min_element[0]
        node = Node("P")
        node.left = first_min_element
        node.right = second_min_element
        node.frequency = merged_frequency
        heapq.heappush(priority_queue, (node.frequency, node))

    root = priority_queue[0]
    code = traverse(root)
    print(code)
    return code
    
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