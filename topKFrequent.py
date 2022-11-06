class Solution:
    def topKFrequent(self, nums, k) :
        numFrequencyList=[]
        numsD=list(set(nums))
        for n in numsD:
            numFrequencyList.append([nums.count(n),n])
        numFrequencyList.sort(reverse=True)
        resp=[]
        for i in range(k):
            resp.append(numFrequencyList[i][1])


        return resp
S=Solution()
print(S.topKFrequent([1],1))