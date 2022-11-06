

class Solution:
    def fillingBucket(self, N):
        # code here
        a, b = 1, 2
        m = 10 ** 8

        if N <= 2: return N

        for i in range(3, N + 1):
            c = (a + b) % m
            a = b
            b = c

        return c

S = Solution()
print(S.fillingBucket(8223))
