from bst_sequences import create_binary_tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_tree_for_sub_tree(root, node):
    left = False
    right = False
    current = validate_sub_tree(root, node)
    if current == True:
        return True
    else:
        if root.left is not None:
            left = check_tree_for_sub_tree(root.left, node)
        if root.right is not None:
            right = check_tree_for_sub_tree(root.right, node)
        if left == True or right == True:
            return True
        else:
            return False

def validate_sub_tree(root_one, root_two):
    if (root_one.value != root_two.value 
        or (root_one.left is not None and root_two.left is not None and validate_sub_tree(root_one.left, root_two.left) == False)
        or (root_one.right is not None and root_two.right is not None and validate_sub_tree(root_one.right, root_two.right) == False)):

        return False
    else:
        return True
    

arr = [2,1,3,4,5,9]
root = create_binary_tree(arr)
print("root: ", root)


print(check_tree_for_sub_tree(root, root.left))
print(check_tree_for_sub_tree(root, Node(100)))