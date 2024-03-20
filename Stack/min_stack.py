class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        # the smaller of val and top of minStack gets appended
        #   Only if minStack exists, if not, val just gets appended
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
        

obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())