import os

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def get_value(self):
        return self.value

    def set_child(self, value):
        self.children.append(value)

    def get_children(self):
        return self.children

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)

a.set_child(b)
a.set_child(c)
b.set_child(d)

tree = Tree(4)
tree.get_root().set_child(a)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    visit_order = list()
    

    return None

def practice(tree):
    visit_order = list()
    root = tree.get_root()
    #recursive function
    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            for child in node.children:
                traverse(child)

    traverse(root)
    return visit_order


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

print(practice(tree))
# Test Case 1
# find_files('.c', "")

# Test Case 2

# Test Case 3