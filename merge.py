class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        num1=-10
        num2=-10
        intervals.sort()
        overlap=[]
        for i in intervals:
            if num2>=i[0]:
                if num1<i[0]:
                    i[0]=num1

                if num2>i[1]:
                    i[1]=num2
                overlap.append([num1,i])              
            num1=i[0]
            num2=i[1]
        for o in overlap:
            if intervals.count(o[1])>1:
                intervals.remove(o[1])
            if intervals.index(o[1])>0 and intervals[intervals.index(o[1])-1].__contains__(o[0]):
                intervals.pop(intervals.index(o[1])-1)
            
        return intervals
