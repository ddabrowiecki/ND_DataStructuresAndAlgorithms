class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        for x in self.groups:
            print(x)
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")


sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(("true" if sub_child_user in sub_child.get_users() else "false"))

class Stack():
    def __init__(self):
        self.list = list()
    
    # add an element to the list
    def push(self,value):
        self.list.append(value)
        
    # remove the last element from the list
    def pop(self):
        return self.list.pop()
        
    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
    
    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0
    
    # 
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_right_child(self):
        return self.right
        
    def get_left_child(self):
        return self.left
        
    def set_right_child(self, node):
        self.right = node
        
    def set_left_child(self, node):
        self.left = node

    def has_right_child(self):
        return self.right != None
        
    def has_left_child(self):
        return self.left != None

    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True
        
    def get_left_child(self):
        return self.left
        
    def set_right_child(self, node):
        self.right = node
        
    def set_left_child(self, node):
        self.left = node

    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    tree = Tree()
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    state = State(node)
    stack.push(state)

    visit_order.append(node.get_value())
    while node:
        if node.has_left_child and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        elif node.has_right_child and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None


    return visit_order

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

sports = Group("sports")
watersports = Group("watersports")
fishing = Group("fishing")
trout_fishing = Group("trout fishing")
bass_fishing = Group("bass fishing")
salmon_fishing = Group("salmon fishing")

tf_1 = "Mark Johns"
trout_fishing.add_user(tf_1)

fishing.add_group(trout_fishing)
fishing.add_group(salmon_fishing)
fishing.add_group(trout_fishing)
watersports.add_group(fishing)
sports.add_group(sports)

assert is_user_in_group(tf_1, watersports) == True

# Test Case 2

# Test Case 3