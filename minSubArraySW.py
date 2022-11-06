class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minL = float('inf')
        i = 0
        j = 0
        currentSum = 0
        while i < len(nums):
            currentSum = currentSum + nums[i]
            i += 1
            while j < i and currentSum >= target:
                currentSum = currentSum - nums[j]
                j += 1
                minL = min (minL, i-j+1)

        return minL


S = Solution()
print(S.minSubArrayLen(40000,[3571,9780,8138,1030,2959,6988,2983,9220,6800,7669,7012,2605,3802,7767,4430]))