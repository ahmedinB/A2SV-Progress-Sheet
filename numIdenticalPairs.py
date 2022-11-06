class Solution(object):
    def AdditiveFactorial(self,nums):
        if nums<2:
            return 0 
        elif nums==2:
            return 1
        elif nums>2:
            return self.AdditiveFactorial(nums-1)+nums-1
        
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=[]
        strNums=[]
        for i in nums:
            strNums.append(str(i))
        
        for n in strNums:
            if strNums.count(n)>1 and int(n) in nums:
                c=strNums.count(n)
                count.append(c)
                for i in range(c):
                    nums.remove(int(n))

        if count != None:
            resp=0
            for i in count:
                resp+=self.AdditiveFactorial(i)
            return resp
        return 0
S=Solution()
print(S.numIdenticalPairs([2,2,5,1,5,5,3,3]))
