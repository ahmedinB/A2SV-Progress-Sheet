class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        median = nums[len(nums)//2]
        l1 = nums[:len(nums)//2]
        l2 = nums[len(nums)//2+1:]
        out = []
        for i in range(len(nums)-1):
            if i%2 != 0 and l1:
                out.append(l1.pop())
            elif i%2 == 0 and l2:
                out.append(l2.pop())
        
        out.append(median)
        if l1 :
            out.append(l1.pop())
        return out
