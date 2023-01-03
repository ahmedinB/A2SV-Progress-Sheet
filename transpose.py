class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        newrow = len(matrix[0]) 
        transpose = []
        for row in range(newrow):
            transpose.append([])
        nr = 0
        for i in matrix:
            for j in i:
                transpose[nr].append(j)
                nr += 1
            nr = 0
            
        return transpose

s = Solution()
print(s.transpose([[1,2,3],[4,5,6]]))
