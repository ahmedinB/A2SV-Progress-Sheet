class Solution:
    def revnum(self, num):
        ans = 0
        while num > 0:
            ans = ans * 10 + num % 10
            num = num // 10
        return ans
    def countDistinctIntegers(self, nums):
        rvnums = set()
        for num in nums:
            rvnums.add(self.revnum(num))

        return len(rvnums.union(set(nums)))

print(Solution().countDistinctIntegers([1,13,10,12,31]))