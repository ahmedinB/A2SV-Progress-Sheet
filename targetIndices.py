class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        indices=[]
        for k in range(0,nums.__len__()):
            if nums[k]==target:
                indices.append(k)
        return indices
