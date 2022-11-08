class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        j = 0
        ans = 1
        for i in range(1,len(nums)):
            reqd = nums[i] - nums[i-1]
            length = (i - j) * reqd
            k -= length
            while k < 0:
                k += nums[i] - nums[j]
                j += 1
            ans = max(ans,i-j+1)
            
        return ans
S=Solution()
print(S.maxFrequency([1,2,4],5))
