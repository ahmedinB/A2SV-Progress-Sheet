class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        intNums=[]
        for i in nums:
            intNums.append([int(i),i])
        intNums.sort(reverse=True)
        print(intNums)
        return str(intNums[k-1])
S=Solution()
print(S.kthLargestNumber(["3","6","7","10"],4))
