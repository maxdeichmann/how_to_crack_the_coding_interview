from copy import copy, deepcopy

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = None
    
    def __str__(self):
        output = ""
        output = output + str(self.value)
        if self.next is not None:
            output = output + " -> " + str(self.next)
        return output
    
    def append_to_tail(self, value):
        currentNode = self
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = Node(value, None)

    def delete_node(self, value):
        currentNode = self
        if currentNode.value is value:
            return currentNode.next
        else:
            while currentNode.next is not None:
                if currentNode.next.value is value:
                    currentNode.next = currentNode.next.next
                    return self
                currentNode = currentNode.next
            return self
        
    def remove_duplicates(self, value):
        currentNode = self
        print(currentNode.value)
        if currentNode.value is value:
            self = currentNode.next
            currentNode = currentNode.next

        while currentNode.next is not None:
            if currentNode.next.value is value:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return self
                
    def k_to_last(self, k):
        n = self
        if k is 0:
            return n
        else:

            count = 0
            while n.next is not None:
                count += 1
                n = n.next
                if k is count:
                    return n

    def delete_middle_node(self):
        length = 0
        n = self
        if n.next is None:
            return n
        else:
            while n.next is not None:
                n = n.next
                length += 1
        

    def delete_at_index(self, index):
        head = self
        n = self
        if index is 0:
            return n.next
        else:
            count = 0
            while n.next is not None:
                count += 1
                if count is index:
                    n.next = n.next.next
                    return head
                n = n.next
            return head


    def partition(self, x):
        n = self
        right = None
        left = None

        if n.next is None:
            return n
        
        else:
            
            while n.next is not None:
                if n.value < x:
                    if right == None:
                        right = Node(n.value, None)
                    else:
                        right.append_to_tail(n.value)
                else:
                    if left == None:
                        left = Node(n.value, None)
                    else:
                        left.append_to_tail(n.value)
                n = n.next
            right.append_to_tail(left)
            return right
    
    def length(self):
        out = 0
        node = self
        while node.next is not None:
            out += 1
            node = node.next

        return out + 1
    
    def get_node_at(self, index):
        if index is 0:
            return self
        else:
            node = self
            count = 0
            while count < index:
                count += 1
                node = node.next
            return node
            

    def is_palindrome(self):
        length = self.length()
        count = (length - 1)/2 if length % 2 == 0 else length / 2
        for i in range(int(count)):
            if self.get_node_at(i).value != self.get_node_at(length-1-i).value:
                return False
        return True
    
    def has_loop(self):
        init = self
        n = init
        while n.next is not None:
            if n.next.next is init:
                return True
            n = n.next
        return False
    
def sum_lists(node_one, node_two):
    return sum([create_int(element) for element in [node_one, node_two]])


def create_int(node):
    values = [node.value]
    while node.next is not None:
        values.append(node.next.value)
        node = node.next

    return sum([element*(10**index) for index, element in enumerate(values)])


def has_intersection(one, two):
    print(one, two)
    if one is two:
        return True
    if one.next is None and two.next is None:
        return one is two
    elif one.next is not None and two.next is None:
        while one.next is not None:
            if two is one.next:
                return True
            one = one.next
        return False
    elif two.next is not None and one.next is None:
        while two.next is not None:
            if one is two.next:
                return True
            two = two.next
        return False
    else:
        while one.next is not None:
            two_copy = two
            while two_copy.next is not None:
                if one is two_copy:
                    return True
                two_copy = two_copy.next
            one = one.next
        return False




head = Node(5, None)
head.append_to_tail(6)
head.append_to_tail(10)
print(head)
new_head = head.delete_node(6)
print(new_head)
head.append_to_tail(5)
head.append_to_tail(5)
new_head = head.remove_duplicates(5)
print(new_head)
head.append_to_tail(6)
head.append_to_tail(11)
print(new_head)
print(new_head.k_to_last(0))
print(new_head.k_to_last(1))
print(new_head.k_to_last(2))
print(new_head)
print(new_head.delete_at_index(2))
new_head.append_to_tail(6)
new_head.append_to_tail(10)
new_head.append_to_tail(5)
new_head.append_to_tail(4)
new_head.append_to_tail(1)
new_head.append_to_tail(9)
new_head.append_to_tail(7)
new_head.append_to_tail(6)
print(new_head)
print(new_head.partition(8))


intersection = Node(100, None)
one = Node(7, None)
one.append_to_tail(1)
one.next.next = intersection

two = Node(5, None)
two.next = intersection
two.append_to_tail(9)
two.append_to_tail(2)

print(sum_lists(one, two))
print(one.length())

pal = Node("C", None)
pal.append_to_tail("B")
pal.append_to_tail("A")
pal.append_to_tail("B")
pal.append_to_tail("C")

print(pal.is_palindrome())

print(has_intersection(one, two))

middle = Node("Middle", None)

pal.next.next.next.next.next = middle
pal.append_to_tail("X")
pal.append_to_tail("y")
pal.append_to_tail("z")
pal.next.next.next.next.next.next.next.next = pal

print(pal.has_loop())