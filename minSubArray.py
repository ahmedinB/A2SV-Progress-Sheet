class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        minL = float('inf')
        for i in range(n):
            sum0 = 0
            for j in range(i, n):
                sum0 += nums[j]
                if sum0 >= target:
                    minL = min(minL, j - i + 1)

        return minL

S = Solution()
print (S.minSubArrayLen(7,[2,1,3,4,5,2]))