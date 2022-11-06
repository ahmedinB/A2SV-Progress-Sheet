class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        i = 0
        largestarea = float('-inf')
        while i < len(heights):
            k = 0
            currentarea = min(heights[i-k:i+1])*len(heights[i-k:i+1])
            print(heights[i-k:i+1])
            if i-k-1 > 0 and  min(heights[i-k-2:i+1])*len(heights[i-k-2:i+1]) > largestarea:
                largestarea = min(heights[i-k-2:i+1])*len(heights[i-k-2:i+1])
            while k < i and  min(heights[i-k-1:i+1])*len(heights[i-k-1:i+1]) > currentarea:
                currentarea = min(heights[i-k-1:i+1])*len(heights[i-k-1:i+1])
                k += 1
            largestarea = max(largestarea, currentarea)
            print(heights[i-k:i+1],heights[i-k-1:i+1] ,k , currentarea)
            i += 1
        return largestarea
S = Solution()
print (S.largestRectangleArea([1,2,4,3,5]))