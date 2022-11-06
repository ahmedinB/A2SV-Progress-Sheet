class Solution(object):
    def calc(self, amount, coins, i):
        if amount< 0 or i < 0:
            return 0
        if amount == 0:
            return 1
        return self.calc(amount-coins[i],coins,i) + self.calc(amount, coins, i-1)

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self.calc(amount, coins, len(coins)-1)


S = Solution()
print(S.change(5 ,[1,2,5]))
