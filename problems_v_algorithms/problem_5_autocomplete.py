#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[102]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
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
        return place


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[106]:


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
    # https://knowledge.udacity.com/questions/146279
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


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[107]:


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
# In[ ]:





# In[108]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:





# In[ ]:





# In[ ]:




