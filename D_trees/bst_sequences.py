from binary_node import in_order_traversal

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)


def create_binary_tree(arr):

    current_node = None

    while len(arr) > 0:
        new_element = arr.pop(0)
        new_node = Node(new_element)
        if current_node is None:
            current_node = new_node
        else:
            append_node_to_tree(current_node, new_node)
    return current_node

def append_node_to_tree(node, new_node):
    if new_node.value > node.value:
        if node.left is None:
            node.left = new_node
        else:
            append_node_to_tree(node.left, new_node)
    if new_node.value < node.value:
        if node.right is None:
            node.right = new_node
        else:
            append_node_to_tree(node.right, new_node)

def create_arrays(root):
    print(root)

    arrays = []

    if root.left is None and root.right is None:
        arrays.append([root.value])
    else:
        left_arrays = []
        right_arrays = []
        if root.left is not None:
            left_arrays = create_arrays(root.left)
        if root.right is not None:
            right_arrays = create_arrays(root.right)
        
        for left in left_arrays:
            for right in right_arrays:
                arrays.append([root.value] + left + right)
                arrays.append([root.value] + right + left)

    return arrays


# arr = [2,1,3,4,5,9]
# root = create_binary_tree(arr)
# in_order_traversal(root)
# print("root: ", root)

# print("-----")

# arr = [2,3,1,4,5,9]
# root = create_binary_tree(arr)
# in_order_traversal(root)
# print("root: ", root)

# print("-----")

# arr = [2,3,1]
# root = create_binary_tree(arr)
# in_order_traversal(root)
# print("root: ", root)
# print(create_arrays(root))

# arr = [2,1,4,3,5]
# root = create_binary_tree(arr)
# in_order_traversal(root)
# print("root: ", root)
# print(create_arrays(root))