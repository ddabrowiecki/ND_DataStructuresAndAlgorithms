## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    # Writing this function was helped by this knowledge board post:
    # https://knowledge.udacity.com/questions/375987
    # I included my original function at the bottom, before I got stuck.
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        for char, node in self.children.items():
            if node.is_word:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        place = self.root
        for char in word:
            if char not in place.children:
                place.children[char] = TrieNode()
            place = place.children[char]
        place.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if type(prefix) != str:
            return "This is not a string."
        place = self.root
        for char in prefix:
            if char not in place.children:
                return "No suffixes for this prefix."
            place = place.children[char]

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

assert (MyTrie.root.children['a'].suffixes()) == ['nt', 'nthology', 'ntagonist', 'ntonym']
assert (MyTrie.root.children['f'].suffixes()) == ['un', 'unction', 'actory']
assert (MyTrie.find('bar')) == "No suffixes for this prefix."
assert (MyTrie.find('x')) == "No suffixes for this prefix."
assert (MyTrie.find(0)) == "This is not a string."

# Previous attempt at solution on my own

# def suffixes(self, suffix = ''):
#         ## Recursive function that collects the suffix for 
#         ## all complete words below this point
#         if self.children is None:
#             suffix = suffix + char
#             return suffix
#         for char in self.children:
#             suffix = suffix + char
#             current_node = self.children[char]
#             current_node.suffixes(suffix)
#         return suffix