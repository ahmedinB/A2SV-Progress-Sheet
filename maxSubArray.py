class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = float('-inf')
        n = len(nums)
        currentsum = 0
        end = 0
        prefixsum = 0
        while end < n:
            currentsum = currentsum + nums[end]
            prefixsum += nums[end]
            maxsum = max(maxsum, currentsum)
            if prefixsum < 0:
                prefixsum = 0
                currentsum = 0
            end += 1
        return maxsum
