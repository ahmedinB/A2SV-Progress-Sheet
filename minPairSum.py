class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=len(nums)-1
        resp=0
        while i>=1:
            if resp < nums[0]+nums[i]:
                resp=nums[0]+nums[i]
            nums.pop(i)
            nums.pop(0)
            i-=2
            
        return resp
