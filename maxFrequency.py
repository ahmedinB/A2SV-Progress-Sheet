class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        maxF=0
        index=0
        for i in range(k):
            if index<len(nums):
                if nums[index]<nums[index+1]:
                    nums[index]=nums[index]+1
                elif nums[index]==nums[index+1] :
                    if index<=1:
                        index-=1
                    else:
                        index+=1
                
                    
                
            print(i, index, nums)
        return nums.count(nums[0])
S=Solution()
print(S.maxFrequency([1,2,4],5))
