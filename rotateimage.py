class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        j, i = len(matrix)-1, 0
        newrows = []
        while i < len(matrix[0]):
            row = []
            while j > -1:
                row.append(matrix[j][i])
                j-=1

            newrows.append(row)
            i+=1
            j=len(matrix)-1
        
        i = 0
        while i < len(newrows):
            matrix[i]= newrows[i]
            i+=1 
        print(matrix)

Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])