from binary_node import in_order_traversal
from random import choices

class Binary_Tree(object):

    def __init__(self):
        self.root = None
        self.size = 0
    
    def __str__(self):
        if self.root is None:
            return "Empty tree"
        else:
            return str(self.root)

    
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        
        def __str__(self):
            output = ""
            if self.left is not None:
                output += " " + str(self.left)
            output += " " + str(self.value)
            if self.right is not None:
                output += " " + str(self.right)
            return output
        
        def get_number_of_nodes(self):
            left = 0
            right = 0
            if self.left is not None:
                left = self.left.get_number_of_nodes()
            if self.right is not None:
                right = self.right.get_number_of_nodes()
            return left+right+1
    
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            current = self.root
            inserted = False
            while inserted == False:
                if value > current.value:
                    if current.right is None:
                        current.right = self.Node(value)
                        inserted = True
                    else:
                        current = current.right
                elif value < current.value:
                    if current.left is None:
                        current.left = self.Node(value)
                        inserted = True
                    else:
                        current = current.left
            self.size += 1
    

    def find(self, value):
        if self.root is None:
            return None
        
        current_node = self.root
        found = False
        while found == False:
            if current_node.value == value:
                return current_node
            elif value < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif value > current_node.value and current_node.right is not None:
                current_node = current_node.right
            else:
                return None
    
    def get_random_node(self):

        current_node = self.root
        selected = False
        
        while selected == False:
            population = [1]
            weights = [1/self.size]
            if current_node.left is not None:
                population.append(2)
                weights.append(current_node.left.get_number_of_nodes()*1/self.size)
            if current_node.right is not None:
                population.append(3)
                weights.append(current_node.right.get_number_of_nodes()*1/self.size)

            result = choices(population, weights)[0]
            #print(population, weights, result)
            if result == 1:
                selected = True
                return current_node
            elif result == 2:
                current_node = current_node.left
            elif result == 3:
                current_node = current_node.right



tree = Binary_Tree()
tree.insert(10)
tree.insert(12)
tree.insert(19)
tree.insert(18)
tree.insert(20)
tree.insert(0)

print(tree)
print(tree.find(20))
print(tree.find(10000))
print(tree.get_random_node())

results = []
for i in range(0, 1000):
    node = tree.get_random_node()
    results.append(node.value)

occurrences = {}
unique_values = set(results)
for val in unique_values:
    occurrences[val] = results.count(val)
print(tree.size, occurrences)


# print(tree.root.value, tree.root.left.value, tree.root.right.value)