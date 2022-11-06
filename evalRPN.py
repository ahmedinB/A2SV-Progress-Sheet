class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = []
        for o in tokens:
            print (ops)
            if o == "+":
                a = ops.pop()
                b = ops.pop()
                ops.append(a + b)
            elif o == "-":
                a = ops.pop()
                b = ops.pop()
                ops.append(b - a)
            elif o == "*":
                a = ops.pop()
                b = ops.pop()
                ops.append(b * a)
            elif o == "/":
                a = ops.pop()
                b = ops.pop()
                ops.append(int(b / a))
            else:
                ops.append(int(o))
        return ops.pop()
S = Solution()
print(S.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))