class MinStack(object):

    def __init__(self):
        self.minstack = []
        self.stack = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        print(self.minstack,self.stack)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) != 0:
            resp=self.stack[-1]
            self.minstack.pop()
            self.stack.pop()
            return resp
    def top(self):
        """
        :rtype: int
        """
        if len(self.minstack) != 0:
            return self.stack[-1]
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minstack) != 0:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

Ms = MinStack()
print(Ms.push(-2))
print(Ms.push(0))
print(Ms.push(-3))
print(Ms.getMin())
print("oppopo",Ms.pop())
print(Ms.top())
print(Ms.getMin())

