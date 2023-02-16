class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = ""
        matrix=[]
        for i in range(len(num1)-1,-1,-1):
            x = ord(num1[i])-48
            mat = []
            rem = 0
            for j in range(len(num2)-1,-1,-1):
                y = ord(num2[j])-48
                if y*x + rem < 10:
                    mat.insert(0, y*x + rem)
                    rem = 0
                elif j==0:
                    mat.insert(0, (y*x + rem))
                    rem = 0
                else:
                    mat.insert(0, (y*x + rem)%10)
                    rem = (y*x + rem)//10
                    
            matrix.append(mat)
        rows = 0 
        indent = len(matrix) - 1
        while rows < len(matrix):
            for i in range(indent):
                matrix[rows].insert(0, 0)
            for i in range(rows):
                matrix[rows].append(0)
            rows += 1
            indent -= 1
        print(matrix)
        resp = 0
        rem = 0
        cols = len(matrix)
        digit = 0
        for index in range(len(matrix[0])-1,-1,-1):
            sum = 0
            for col in range(cols):
                sum += matrix[col][index]
            resp += sum * 10**digit
            digit += 1
        return resp



S = Solution()
print(S.multiply("123","456"))
print(S.multiply("98", "9"))
print(S.multiply("3", "514"))

##   failed this case because the reminders are not separated

