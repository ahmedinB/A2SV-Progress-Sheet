class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        
        for index in range(len(nums1) - m):
            nums1.pop()
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                i += 1
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                m += 1
            elif nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                m += 1  
        while j < n:
            i += 1
            nums1.insert(i, nums2[j])
            j += 1
        
        
