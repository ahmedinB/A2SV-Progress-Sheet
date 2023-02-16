class Solution:
    def spiralOrder(self, matrix):

        spiralmatrix = []
        n = len(matrix)
        m = len(matrix[0])
        elements = n * m
        count = 0
        direction = "right"
        turns = 0
        cycle = 0
        cycle0 = 0
        i, j = 0, 0
        while count < elements:
            if direction == "right":
                if j == m - 1 - cycle:
                    direction = "down"
                    turns += 1
                else:
                    spiralmatrix.append(matrix[i][j])
                    count += 1
                    j += 1
            elif direction == "down":
                if i == n - 1 - cycle :
                    direction = "left"
                    turns += 1
                else:
                    spiralmatrix.append(matrix[i][j])
                    count += 1
                    i += 1
            elif direction == "left":
                if  j == cycle:
                    direction = "up"
                    turns += 1
                else:
                    spiralmatrix.append(matrix[i][j])
                    count += 1
                    j -= 1
            elif direction == "up":
                if i-1 == cycle:
                    direction = "right"
                    turns += 1
                    cycle += 1
                else:
                    spiralmatrix.append(matrix[i][j])
                    count += 1
                    i -= 1


        return spiralmatrix
        # cycle increament after three turns
        # start by right until j = m-1-cycle
        # down  til i = m - 1-cycle
        # left til


# print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[1,2,3,4],
                              [5,6,7,8],
                              [9,10,11,12],
                              [13,14,15,16]]))
print(Solution().spiralOrder([[1,2,3,4,5],
                              [6,7,8,9,10],
                              [11,12,13,14,15],
                              [16,17,18,19,20],
                              [21,22,23,24,25]]))
print(Solution().spiralOrder([[1,2,3,4,5,6,7,8,9,10],
                              [11,12,13,14,15,16,17,18,19,20],
                              [21,22,23,24,25,26,27,28,29,30],
                              [31,32,33,34,35,36,37,38,39,40],
                              [41,42,43,44,45,46,47,48,49,50],
                              [51,52,53,54,55,56,57,58,59,60],
                              [61,62,63,64,65,66,67,68,69,70],
                              [71,72,73,74,75,76,77,78,79,80],
                              [81,82,83,84,85,86,87,88,89,90],
                              [91,92,93,94,95,96,97,98,99,100]]))