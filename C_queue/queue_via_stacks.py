from stack import MyStack

class QueueOverFlow(Exception):
   """Raised when stack is empty"""
   pass

class EmptyQueueExeption(Exception):
   """Raised when stack is empty"""
   pass

class MyQueue(object):

    def __init__(self, capacity):
        self.output_stack = MyStack(capacity)
        self.help_stack = MyStack(capacity)
        self.capacity = capacity
        self.current_capacity = capacity

    def __str__(self):
        output = "Queue: "+str(self.output_stack) + "\n"
        output += "Helper: "+str(self.help_stack)
        return output

    def add(self, value):
        if self.current_capacity > 0:
            if self.output_stack.is_empty() == True:
                self.output_stack.push(value)
            else:
                while self.output_stack.is_empty() == False:
                    self.help_stack.push(self.output_stack.pop())
                self.output_stack.push(value)
                self.current_capacity -= 1
                while self.help_stack.is_empty() == False:
                    self.output_stack.push(self.help_stack.pop())
        else:
            raise QueueOverFlow
    
    def remove(self):
        try:
            return self.output_stack.pop()
        except:
            raise EmptyQueueExeption


qu = MyQueue(10)
qu.add(0)
qu.add(1)
qu.add(2)
qu.add(3)
qu.add(4)

print(qu)

print(qu.remove())
print(qu.remove())
print(qu.remove())
print(qu.remove())
print(qu.remove())
print(qu.remove())

