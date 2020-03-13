from binary_node import in_order_traversal

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

def create_tree(arr):

    middle = int(len(arr)/2)
    new_node = Node(arr[middle])
    if len(arr[:middle]) > 0:
        new_node.left = create_tree(arr[:middle])
    if len(arr[middle + 1:]) > 0:
        new_node.right = create_tree(arr[middle + 1:])
    return new_node


def find_common_ancestor(n1, n2, root):

    found = False
    while found == False:
        if (is_in_node(root.left, n1) == True and is_in_node(root.right, n2) == True) or (is_in_node(root.right, n1) == True and is_in_node(root.left, n2) == True):
            found == True
            return root
        elif is_in_node(root.left, n1) == True and is_in_node(root.left, n2) == True:
            root = root.left
        elif is_in_node(root.right, n1) == True and is_in_node(root.right, n2) == True:
            root = root.right
        else:
            return None
    return None


def is_in_node(root, value):
    if root.value == value:
        return True
    elif root.left is not None and is_in_node(root.left, value) == True:
        return True
    elif root.right is not None and is_in_node(root.right, value) == True:
        return True
    
    return False


arr = [5,8,3,5,89,0,7,4,2,5,7,9,564,2,456,78,976,54,323,456]

# create tree
tree = create_tree(arr)

left = tree.left.left.left.left
right = tree.left.right.left
#in_order_traversal(tree)
print(">>>", tree.left.value, find_common_ancestor(left.value, right.value, tree))