class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        longest = float('-inf')
        start = 0
        end = 0
        if max(nums)-min(nums)<limit:
            return len(nums)
        while end < len(nums) :
            m = max(nums[start:end+1])
            mn = min(nums[start:end+1])
            if m-mn <= limit:
                longest = max (len (nums[start:end+1]),longest)
            else:
                start += 1
            end += 1
        return longest
S = Solution()
print (S.longestSubarray( [10,1,2,4,7,2],5))