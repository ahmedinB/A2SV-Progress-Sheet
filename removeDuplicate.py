class Solution:
    def removeDuplicates(self, nums):
        i = 0
        ans = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                ans+=1
                i-=1
            i+=1
        print(nums)
        return ans

print(Solution().removeDuplicates([1,1,2]))