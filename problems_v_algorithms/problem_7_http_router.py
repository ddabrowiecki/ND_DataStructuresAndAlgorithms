# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

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

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.route_trie.handler
        if path[-1] == "/":
            path = path[:-1]
        if not self.route_trie.find(path):
            return self.not_found_handler
        else:
            return self.route_trie.find(path)


    # def split_path(self, ...):
    #     # you need to split the path into parts for 
    #     # both the add_handler and loopup functions,
    #     # so it should be placed in a function here

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one