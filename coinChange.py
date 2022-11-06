class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1

        dp = {}
        coins.sort(reverse=True)

        def rec(remaining, ci):
            if ci >= len(coins):
                return 0

            if remaining in dp and ci in dp[remaining]:
                return dp[remaining][ci]

            if remaining == 0:
                return 1

            elif remaining < 0:
                return 0

            number_of_ways = rec(remaining - coins[ci], ci)

            for nci in range(ci + 1, len(coins)):
                number_of_ways += rec(remaining - coins[nci], nci)

            if remaining in dp:
                dp[remaining][ci] = number_of_ways
            else:
                dp[remaining] = {ci: number_of_ways}

            return number_of_ways

        return rec(amount, 0)
S = Solution()
print(S.change(20,[1,2,5]))
