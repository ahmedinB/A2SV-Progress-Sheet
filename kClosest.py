import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        li= []
        for x, y in points:
            li.append([x**2+y**2, x, y])      
        li.sort()
        result = []
        for i in range(k):
            
            result.append([li[i][1],li[i][2]])
            
        return result   
