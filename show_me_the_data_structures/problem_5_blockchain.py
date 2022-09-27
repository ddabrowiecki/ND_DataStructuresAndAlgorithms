import hashlib
import datetime
import pprint

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = self.create_timestamp()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
        if data is None:
            return ''

        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def create_timestamp(self):
        current_time = datetime.datetime.utcnow()
        return current_time

class Blockchain:

    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        block = self.head
        block_data = {}
        while block:
            block_data["data"] = block.data
            block_data["timestamp"] = block.timestamp
            block_data["previous_hash"] = block.previous_hash
            block_data["hash"] = block.hash 
            out.append(block_data)
            block_data = {}
            block = block.next
        return out
    
    def add_block(self, data):
        if self.head is None:
            self.head = Block(data, previous_hash=None)
            return

        block = self.head
        while block.next:
            block = block.next
        current_hash = block.hash
        block.next = Block(data, previous_hash=current_hash)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1 -- Regular case
blockchain = Blockchain()
blockchain.add_block('This is the first block')
blockchain.add_block('This is the second block')
blockchain.add_block('This is the third block')
blockchain_list = blockchain.to_list()

first_block_hash = blockchain_list[0]["hash"]
second_block_hash = blockchain_list[1]["hash"]

assert blockchain_list[0]["previous_hash"] == None
assert blockchain_list[1]["previous_hash"] == first_block_hash
assert blockchain_list[2]["previous_hash"] == second_block_hash

# Test Case 2 -- Null Value, block chain should continue
test_1_blockchain = Blockchain()
test_1_blockchain.add_block('This is the first block')
test_1_blockchain.add_block(None)
test_1_blockchain.add_block('This is the third block')
test_1_blockchain_list = test_1_blockchain.to_list()

assert test_1_blockchain_list[1]["data"] == None
assert test_1_blockchain_list[1]["previous_hash"] == test_1_blockchain_list[0]["hash"]
assert test_1_blockchain_list[2]["previous_hash"] == test_1_blockchain_list[1]["hash"]

# Test Case 3 -- Large value
test_2_blockchain = Blockchain()
test_2_blockchain.add_block("first block")
test_2_blockchain.add_block("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
test_2_blockchain.add_block("third block")
test_2_blockchain_list = test_1_blockchain.to_list()

assert test_2_blockchain_list[1]["data"] == None
assert test_2_blockchain_list[1]["previous_hash"] == test_2_blockchain_list[0]["hash"]
assert test_2_blockchain_list[2]["previous_hash"] == test_2_blockchain_list[1]["hash"]