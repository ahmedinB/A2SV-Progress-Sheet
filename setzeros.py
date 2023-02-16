import copy

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix0 = copy.deepcopy(matrix)
        for col in range(len(matrix[0])):
            zero = False
            for row in range(len(matrix)):
                if matrix[row][col]==0:
                    zero=True

            if zero:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        for row in range(len(matrix)):
            if 0 in matrix0[row]:
                matrix[row] = [0]*len(matrix[0])


        print(matrix)

Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])