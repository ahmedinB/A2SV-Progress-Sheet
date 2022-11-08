class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        resp=[]
        for i in range(len(l)) :
            resp.append(self.checkArithmetic(nums[l[i]:1+r[i]]))
        
        return resp

    def checkArithmetic(self,nums):
        nums.sort()
        d=nums[1]-nums[0]
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]-d:
                print (d,nums[i],nums[i+1])
                return False
            
        return True
