class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resp = -1
        totalSum = sum(nums)
        prefixSum = 0
        for i in range(len(nums)):
            if totalSum == 2*(prefixSum) + nums[i]:
                resp = i
            prefixSum += nums[i]
            print(prefixSum)
        return resp

##class Solution:
##    def pivotIndex(self, nums: List[int]) -> int:
##        
##        totalSum = sum(nums)
##        ans = -1
##        prefix_sum = 0
##        for i in range(len(nums)):
##            if 2 * prefix_sum + nums[i] == totalSum:
##                return i
##            prefix_sum += nums[i]
##        return ans
    #[1,7,3     ,6,    5,6] = totalSum =  28
      # 1 8 11

S = Solution()
print(S.pivotIndex([1,2,3]))
