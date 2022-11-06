class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.CQ = [None]*k
        self.front = 0
        self.last = 0
        self.k=k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.CQ[0] = value
            self.front=0
            self.last=0
            return True

        if self.front == 0:
            front = self.k-1
        else:
            front = self.front-1
        # if self.front-1 == self.last:
        #     self.last = (self.last+1) % self.k

        if self.CQ[front] is None:

            self.CQ[front] = value
            self.front = front
            return True
        else :
            return False
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.CQ[0] = value
            self.front = 0
            self.last = 0
            return True

        last = (self.last+1) % self.k

        if self.CQ[last] is None:
            self.CQ[last] = value
            self.last = last
            return True
        else :
            return False
    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.CQ[self.front] is not None:
            self.CQ[self.front] = None
            if self.last == self.front:
                if self.last == 0:
                    self.last = self.k - 1
                else:
                    self.last -= 1
            self.front = (self.front+1) % self.k

            return True
        else:
            return False
    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.CQ[self.last] is not None:
            self.CQ[self.last] = None
            if self.last == self.front:
                self.last = (self.last + 1) % self.k
            if self.last == 0:
                self.last = self.k - 1
            else:
                self.last -= 1

            return True
        else:
            return False
    def getFront(self):
        """
        :rtype: int
        """
        if self.CQ[self.front] is not None:
            return self.CQ[self.front]
        else:
            return -1
    def getRear(self):
        """
        :rtype: int
        """
        if self.CQ[self.last] is not None:
            return self.CQ[self.last]
        else:
            return -1
    def isEmpty(self):
        """
        :rtype: bool
        """
        for i in self.CQ:
            if i is not None:
                return False
        return True
    def isFull(self):
        """
        :rtype: bool
        """
        for i in self.CQ:
            if i is None:
                return False
        else:
            return True

    def printQ(self):
        print( self.CQ, self.last, self.front)
# Your MyCircularDeque object will be instantiated and called as such:
# ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]
# [[3],[1],[2],[3],[4],[],[],[],[4],[]]

obj = MyCircularDeque(3)
obj.printQ()
param_1 = obj.insertLast(1)
obj.printQ()
param_2 = obj.insertLast(2)
obj.printQ()
param_3 = obj.insertFront(3)
obj.printQ()
param_4 = obj.insertFront(4)
obj.printQ()
param_5 = obj.getRear()
obj.printQ()
param_6 = obj.isFull()
obj.printQ()
param_7 = obj.deleteLast()
obj.printQ()
param_8 = obj.insertFront(4)
obj.printQ()
param_9 = obj.getFront()
obj.printQ()
# param_95 = obj.insertLast(4)
# param_10 = obj.isEmpty()
print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9) # , param_95,param_10)

# [null,true,true,true,false,2,true,true,true,4]