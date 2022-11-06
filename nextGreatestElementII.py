class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        n = len(nums)
        resp = []
        while i < n:
            j = 0
            greater = False
            while j < n:
                if nums[i] < nums[(i+j+1)%n]:
                    resp.append(nums[(i+j+1)%n])
                    greater = True
                    break
                j+=1
            if not greater:
                resp.append(-1)
            i+=1
        return resp
S = Solution()
print(S.nextGreaterElements([1,2,3,4,3]))