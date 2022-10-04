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

class Tree(Node):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")  # root node

# set first level's left child
tree.get_root().set_left_child(Node("banana"))  

# set first level's right child
tree.get_root().set_right_child(Node("cherry"))  

# set second level's left child 
# by getting the first level's left child first
tree.get_root().get_left_child().set_left_child(Node("dates"))

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

# instantiate Stack
stack = Stack()
# add elements into the stack
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
# remove and print the last element (top of the stack)

visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)

# visit apple (root)
visit_order.append(node.get_value())

# check if apple (root) has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# visit banana (first level's left child)
visit_order.append(node.get_value())

# check if banana has a left child (second level's left chile)
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()    
    stack.push(node)

# visit dates (second level's left chile)
visit_order.append(node.get_value())

# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
stack.pop()

# now we'll set the node to the new top of the stack, which is banana
node = stack.top()

# now we'll track the new top of the stack, which is apple
node = stack.top()

if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)

visit_order.append(node.get_value())

print(f"""stack
{stack}""")

###########################################

def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    stack.push(node)
    node = stack.top()
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit): 
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
        """)
        count +=1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node)
            # using top() is redundant, but added for clarity
            node = stack.top() 
            visit_order.append(node.get_value())
            
        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None
        
        
    return visit_order

pre_order_with_stack_buggy(tree)

def pre_order(tree):
    