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
    file_visit_order = list()
    folder_visit_order = list()
    #recursive function
    def traverse(node):
        if node.startswith('subsub'):
            print(os.path.isdir(node))
        if node.endswith(suffix):
            pass
            # visit_order.append(node)
        if os.path.isdir(node):
            for child in os.listdir(node):
                traverse(child)
    traverse(path)
    return visit_order


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

path = './testdir'
os.chdir(path)
cwd = os.getcwd()

# Test Case 1
print(find_files('.c', cwd))

# Test Case 2

# Test Case 3