
class EmptyHeapException(Exception):
   """Raised when stack is empty"""
   pass



class MyHeap(object):
    class HeapNode(object):
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def __str__(self):
            return str(self.data)

    top = None

    def __str__(self):
        if self.top is None:
            return "is_empty = true" 
        else:
            output = ""
            output = output + str(self.top)
            n = self.top
            while n.next is not None:
                output = output + " -> " + str(n.next)
                n = n.next
            return output

    def remove(self):
        if self.top is None:
            raise EmptyHeapException
        else:
            node = self.top
            while node.next is not None:
                if node.next.next is None:
                    val = node.next.data
                    node.next = None
                    return val
                node = node.next

    def add(self, data):
        new_node = self.HeapNode(data)
        if self.top is None:
            self.top = new_node
        else:
            node = self.top
            while node.next is not None:
                node = node.next            
            node.next = new_node
    

    def peek(self):
        if self.top is None:
            raise EmptyHeapException
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None

    

hp = MyHeap()
print(hp.is_empty())
hp.add(2)
hp.add(4)
hp.add(6)

print(hp)
print(hp.remove())
print(hp)
hp.add(6)
print(hp)
print(hp.is_empty())
print(hp.peek())