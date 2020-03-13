
class EmptystackException(Exception):
   """Raised when stack is empty"""
   pass

class StackOverFlow(Exception):
   """Raised when stack is empty"""
   pass



class MyStack(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = capacity

    class StackNode(object):
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

    def pop(self):
        if self.top is None:
            raise EmptystackException
        else:
            val = self.top.data
            self.top = self.top.next
            self.current_capacity += 1
            return val

    
    def push(self, data):
        new_node = self.StackNode(data)
        if self.top is None:
            self.top = new_node
            self.current_capacity -= 1
        else:
            if self.current_capacity > 1:
                new_node.next = self.top
                self.top = new_node
                self.current_capacity -= 1
            else:
                raise StackOverFlow

    

    def peek(self):
        if self.top is None:
            raise EmptystackException
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None

    def min(self):
        return self.top
    
    def push_min(self, data):
        new_node = self.StackNode(data)
        if self.top is None:
            self.top = new_node
        else:
            if self.top.data > new_node.data:
                new_node.next = self.top
                self.top = new_node
            else:
                new_node.next = self.top.next
                self.top.next = new_node

    def get_current_capacity(self):
        return self.current_capacity

    
    def sort(self):
        if self.is_empty():
            return self
        else:
            help_stack = MyStack(self.capacity)
            while self.is_empty() == False:
                top_element = self.pop()
                if help_stack.is_empty() == True:
                    help_stack.push(top_element)
                else:
                    while help_stack.is_empty() == False and top_element < help_stack.peek():
                        poped = help_stack.pop()
                        self.push(poped)

                    help_stack.push(top_element)
            
            while help_stack.is_empty() == False:
                self.push(help_stack.pop())






    

# st = MyStack(100)
# print(st.is_empty())
# st.push(4)
# st.push(6)
# st.push(2)
# st.push(10)
# st.push(100)
# st.push(1)
# st.push(8)
# st.push(3)
# st.sort()
# print(st)

# print(st)
# st.pop()
# print(st)
# st.push(6)
# print(st.is_empty())
# print(st.peek())