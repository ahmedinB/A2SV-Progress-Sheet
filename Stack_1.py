class MyQueue(object):

    def __init__(self):
        self.Q=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.Q) != 0:
            resp=self.Q[0]
            self.Q.pop(0)
            return resp

    def peek(self):
        """
        :rtype: int
        """
        if len(self.Q) != 0:
            return self.Q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.Q) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

MyQueue = MyQueue()

print(MyQueue.push(1))
print(MyQueue.push(2))
print(MyQueue.peek())
print(MyQueue.pop())
print(MyQueue.empty())






