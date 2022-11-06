class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        k = 2
        currentsum = sum(nums[:k])
        while i < len(nums)-k :
            if currentsum == target:
                return [i,i+1]
            currentsum = currentsum - nums[i] + nums[i+k]
            i += 1

S = Solution()
print (S.twoSum([3,2,3,3],6))