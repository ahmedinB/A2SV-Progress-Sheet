class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i = 0
        # j = 1
        # while i < len(nums) and j < len(nums):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]
        #     if nums[i] * 2 == target and nums.count(nums[i]) == 2:
        #         return [i, j]
        #     if j == len(nums) - 1:
        #         i += 1
        #         j = i + 1
        #     else:
        #         j += 1
        i = len(nums) - 1
        j = i - 1
        print(i,j, len(nums))
        while i >= 0 and j >= 0:
            if nums[i] + nums[j] == target:
                return [i, j]
            # duplicate case solution
            print (i,j,nums[i],nums[j])
            if j == 0:
                i -= 1
                j = i - 1
            else:
                j -= 1


S = Solution()
print (S.twoSum([2,7,11,15],6))