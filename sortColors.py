lass Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,nums.__len__()):
            for j in range(0,nums.__len__()):
                if nums[i]<nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
