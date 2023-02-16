class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                i += 1
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            elif nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            print("case!", nums1,nums2,i,j)
        while j < n:
            i += 1
            nums1.insert(i, nums2[j])
            j += 1
            
        
        return nums1[:n+m]

S = Solution()
print(S.merge([1,2,3,0,0,0],3,[2,5,6],3))
