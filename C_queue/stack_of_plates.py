from stack import MyStack


# should be better to solve via a stack and not an array!!!
class SetOfStacks(object):


    def __init__(self, capacity_per_stack):
        self.capacity_per_stack = capacity_per_stack
        self.stack = MyStack(100)
        self.stack.push(MyStack(capacity_per_stack))

    def __str__(self):
        return str(self.stack)


    def push(self, value):
        top = self.stack.peek()
        if top.get_current_capacity() > 1:
            top.push(value)
        else:
            self.stack.push(MyStack(self.capacity_per_stack))
            self.stack.peek().push(value)
    
    def pop(self):
        top = self.stack.peek()
        val = top.pop()
        if top.get_current_capacity() > self.capacity_per_stack - 1:
            self.stack.pop()
        return val



st = SetOfStacks(3)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.push(7)
print(st)

print(st.pop())
print(st.pop())

print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())

