from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix):
        ddict = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if ddict[j-i]==[]:
                    ddict[j-i] = [True, matrix[i][j]]
                elif ddict[j-i][0] == True and ddict[j-i][1] != matrix[i][j]:
                    return False
        return True

print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))