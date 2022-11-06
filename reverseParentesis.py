class Solution:

    def reverseParentheses(self, s: str) -> str:
        s0 = [""]
        for i in s:
            if i == "(" :
                s0.append("")
            elif  i == ")":
                s0[len(s0)-2] += s0.pop()[::-1]
            else:
                s0[-1] += i
        return "".join(s0)
S = Solution()
print(S.reverseParentheses("(ed(et(oc))el)"))
print(S.reverseParentheses("a(bcdefghijkl(mno)p)q"))
# "apmnolkjihgfedcbq"