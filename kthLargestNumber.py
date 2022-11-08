class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        intNums=[]
        for i in nums:
            intNums.append([int(i),i])
        intNums.sort(reverse=True)
        
        return str(intNums[k-1][1])
