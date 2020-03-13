from binary_node import in_order_traversal


class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return str(self.value)


    def insert(self, value):
        
        # find last element
        current_node = self
        while current_node.left is not None and current_node.right is not None:
            if current_node.right is not None:
                current_node = current_node.right
            else:
                current_node = current_node.left

        print(current_node)

        # insert at last position
        if current_node.left is None:
            current_node.left = Node(value, current_node)
            self.bubble_up(current_node)
            print("call left")
        elif current_node.right is None:
            print("call right")
            current_node.right = Node(value, current_node)
            self.bubble_up(current_node)

    
    
    def bubble_up(self, node):
        print("bubble")
        current_node = self

        if current_node.left is not None and current_node.left.value <= current_node.value:
            print("left is smaller then self")
            temp = current_node.left.value
            current_node.left.value = current_node.value
            current_node.value = temp
            self.bubble_up(current_node)
        
        if current_node.right is not None and current_node.right.value > current_node.value:
            print("right is smaller then self")
            temp = current_node.right.value
            current_node.right.value = current_node.value
            current_node.value = temp
            self.bubble_up(current_node)
        
        if current_node.parent is not None:
            self.bubble_up(current_node.parent)

def min_value(node):
    top_node = node
    while top_node.parent is not None:
        top_node = top_node.parent
    
    last_node = node
    while last_node.left is not None and last_node.right is not None:
        if last_node.right is not None:
            last_node = last_node.right
        else:
            last_node = last_node.left
    
    last_node.left = node.left
    last_node.right = node.right
    node = node
    print(node)
    return node




root = Node(5, None)
# root.right = Node(8, )
# root.left = Node(10)
# root.left.left = Node(70)
# root.left.right = Node(900)
# root.right.left = Node(100)

#                5
#         10          8
#      70   900   100    9000

root.insert(2)
root.insert(1000)
root.insert(1)

print(">>>>")
print(root.value)
print("left", root.left)
print("right", root.right)
in_order_traversal(root)

new_node = min_value(root)
print("new_node", new_node)
# root.insert(10)
# print(">>>>")
# in_order_traversal(root)
# root.insert(10)
# root.insert(100)
# root.insert(9)

