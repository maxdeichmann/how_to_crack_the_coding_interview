class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self):
        return str(self.value)
    
# print left branch, current node, right branch
def in_order_traversal(node):

    if node.left is not None:
        in_order_traversal(node.left)
    print(node.value)

    if node.right is not None:
        in_order_traversal(node.right)

def pre_order_traversal(node):
    print(node.value)

    if node.left is not None:
        in_order_traversal(node.left)

    if node.right is not None:
        in_order_traversal(node.right)

def post_order_traversal(node):

    if node.left is not None:
        in_order_traversal(node.left)

    if node.right is not None:
        in_order_traversal(node.right)

    print(node.value)

def create_search_tree(arr):
    
    mid = int(len(arr)/2) if len(arr) % 2 == 0 else int((len(arr)-1)/2)
    new_node = Node(arr[mid])
    if len(arr[:mid]) > 0:
        new_node.left = create_search_tree(arr[:mid])
    if len(arr[mid+1:]) > 0:
        new_node.right = create_search_tree(arr[mid+1:])
    return new_node

def list_of_depths(root):

    routes = []
    stack = [[root]]

    while len(stack) > 0:
        current_route = stack.pop()
        adjacent_nodes = []
        
        if hasattr(current_route[-1], "right") and current_route[-1].right is not None:
            adjacent_nodes.append(current_route[-1].right)
        if hasattr(current_route[-1], "left") and current_route[-1].left is not None:
            adjacent_nodes.append(current_route[-1].left)

        if len(adjacent_nodes) > 0:
            for element in adjacent_nodes:
                new_route = current_route + [element]
                stack.append(new_route)
        else:
            routes.append(current_route)

    result = {}
    for route in routes:
        for i, element in enumerate(route):
            if i in result:
                if element.value not in result[i]:
                    result[i].append(element.value)
            else:
                result[i] = [element.value]
    return result

def check_balanced(tree):
    right_check = True
    left_check = True

    right = 0
    left = 0

    if tree.right is not None:
        right += 1
        if tree.right.right is not None or tree.right.left is not None:
            right += 1
    if tree.left is not None:
        left += 1
        if tree.left.right is not None or tree.left.left is not None:
            left += 1
    
    if tree.left is not None:
        left_check = check_balanced(tree.left)

    if tree.right is not None:
        right_check = check_balanced(tree.right)
    

    if abs(right-left) > 1 or right_check == False or left_check == False:
        return False
    else:
        return True
    
def check_binary_search_tree(tree):

    left = True
    right = True
    if tree.left is not None:
        left = check_node_values(tree.left)

    if tree.right is not None:
        right = check_node_values(tree.right)
    
    if right == False or left == False or check_node_values(tree) == False:
        return False
    else:
        return True

def check_node_values(tree):
    validation = True

    if tree.left is not None:
        if tree.left.value > tree.value:
            validation = False
    if tree.right is not None:
        if tree.right.value < tree.value:
            validation = False
    return validation

def find_left_most_node(node):
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node

def in_order_successor(node):
    if node.right is not None:
        return find_left_most_node(node.right)
    else:
        if node.parent is not None and node.parent.left is not None and node.parent.left.value == node.value:
            return node.parent
        
        else:
            # go up until we are not left anymore
            if node.parent is not None:
                current_node = node
                parent = current_node.parent

                while parent.parent is not None and current_node.value !=  parent.left.value:
                    current_node = parent
                    parent = parent.parent
                
                return parent

# TRAVERSALS
# root = Node(5)
# root.right = Node(8)
# root.left = Node(10)
# root.right.right = Node(100)
# root.right.left = Node(70)
# root.left.right = Node(900)

# in_order_traversal(root)
# print("-----")
# pre_order_traversal(root)
# print("-----")
# post_order_traversal(root)

# CREATE SEARCH TREE
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# root = create_search_tree(arr)
# in_order_traversal(root)

# LIST OF DEPTHS
# print(list_of_depths(root))

# CHECK BALANCE
# arr = [1,2,3]
# root = create_search_tree(arr)
# root.right.right = Node(9)
# root.right.right.right = Node(10)
# in_order_traversal(root)
# print(check_balanced(root))

# CHECK BINARY SEARCH TREE
# arr = [1,2,3]
# root = create_search_tree(arr)
# root.right.right = Node(100000)
# print(check_binary_search_tree(root))