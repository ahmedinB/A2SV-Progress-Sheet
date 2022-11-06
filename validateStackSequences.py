class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for n in pushed :
            stack.append(n)
            while len(stack) > 0 and stack[-1]==popped[i]:
                stack.pop(-1)
                i += 1
        return len(stack) == 0
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
# [0,2,1]
# [0,1,2]
S = Solution()
print(S.validateStackSequences([0,2,1],[0,1,2]))
