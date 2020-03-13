
class EmptyStackException(Exception):
   """Raised when stack is empty"""
   pass

class ThreeInOneStack(object):
    def __init__(self, size):
        self.stack = [None] * size
        first = int(size/3)
        second = first * 2
        third = size
        self.borders = [first, second, third]
    

    def add(self, stack_index, value):
        last_element = self.borders[stack_index]
        first_element = 0 if stack_index - 1 < 0 else self.borders[stack_index - 1]

        if self.stack[last_element-1] is not None:
            raise EmptyStackException
        else:
            print(range(first_element, last_element - 1))
            for i in reversed(range(first_element, last_element - 1)):
                self.stack[i+1] = self.stack[i]
                if i == first_element:
                    self.stack[i] = value
    
    def remove(self, stack_index):
        last_element = self.borders[stack_index]
        first_element = 0 if stack_index - 1 < 0 else self.borders[stack_index - 1]
        
        val = self.stack[first_element]
        for i in range(first_element, last_element):
            if i != last_element-1:
                self.stack[i] = self.stack[i+1]
            else:
                self.stack[i] = None
        return val


tioSt = ThreeInOneStack(12)
tioSt.add(0, 1)
print(tioSt.stack, tioSt.borders)
tioSt.add(0, 2)
print(tioSt.stack, tioSt.borders)
tioSt.add(0, 3)
print(tioSt.stack, tioSt.borders)
tioSt.add(0, 4)
print(tioSt.stack, tioSt.borders)
tioSt.add(1, 5)
print(tioSt.stack, tioSt.borders)
print(tioSt.remove(0))
print(tioSt.stack, tioSt.borders)