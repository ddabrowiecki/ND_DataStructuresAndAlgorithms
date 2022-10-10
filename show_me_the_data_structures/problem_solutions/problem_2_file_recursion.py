import os

# Got inspiration from this mentor help post, which resembles my original solution at the bottom:
# https://knowledge.udacity.com/questions/447861
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
    files = list()
    folders = list()
    # Look through all nodes of the path. Separate files and folders.
    for node in os.listdir(path):
        if node.endswith(suffix):
            files.append(node)
        if "." not in node:
            folders.append(node)
    for folder in folders:
        files.extend(find_files(suffix, path + "/" + folder ))
    return files


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

path = os.getcwd() + '/testdir'

# Test Case 1
print(find_files('.c', path))

# Expected solution: ['t1.c', 'b.c', 'a.c', 'a.c']

# Test Case 2

# Test Case 3


# Original attempt at recursive solution

    # visit_order = list()
    # def traverse(node):
    #     if node.startswith('subsub'):
    #         print(os.path.isdir(node))
    #     if node.endswith(suffix):
    #         visit_order.append(node)
    #     if os.path.isdir(node):
    #         for child in os.listdir(node):
    #             traverse(child)
    # traverse(path)
    # return visit_order