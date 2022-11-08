class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            smallerNums=0
            for j in nums:
                if i>j:
                    smallerNums+=1
            l.append(smallerNums)
        return l
                    
