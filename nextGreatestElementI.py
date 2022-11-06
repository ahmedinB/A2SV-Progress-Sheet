class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i = 0
        resp = []
        while i < len(nums1):
            # nums2.index[nums1[i]]
            greater = False
            for j in range(nums2.index(nums1[i]),len(nums2)-1):
                if nums1[i] < nums2[j+1]:
                    resp.append(nums2[j+1])
                    greater=True
                    break
            if not greater :
                resp.append(-1)
            i+=1



        return resp


S = Solution()
print (S.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))

