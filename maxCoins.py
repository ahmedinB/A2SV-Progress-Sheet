class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        i=len(piles)
        resp=0
        while i>=2:
            piles.sort()
            chosen=[piles[0],piles[i-2],piles[i-1]]
            resp+=chosen[1]
            piles.pop(i-1)
            piles.pop(i-2)
            piles.pop(0)
            i-=3
        return resp
        
        
        

S=Solution()
print(S.maxCoins([9,8,7,6,5,1,2,3,4]))
## [2,4,5]
