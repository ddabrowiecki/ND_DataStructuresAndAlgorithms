# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = "route_trie_handler"

    def insert(self, path, handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # Checked my function with this post: https://knowledge.udacity.com/questions/352696 
        current_node = self.root
        separated_path = path.split("/")
        for path_chunk in separated_path:
            if path_chunk not in current_node.children:
                current_node.children[path_chunk] = RouteTrieNode()
                current_node = current_node.children[path_chunk]
            current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        separated_path = path.split("/")
        for path_chunk in separated_path:
            if path_chunk not in current_node.children:
                return None
            current_node = current_node.children[path_chunk]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=""):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path_chunk):
        # Insert the node as before
        self.children[path_chunk] = RouteTrieNode()

dom = RouteTrie()
dom.insert('dom/about/me', "about_me_handler")
print(dom.find('dom/about/me'))