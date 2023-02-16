from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        for row in board:
            for item in row:
                if item!= "." and row.count(item)>1:
                    return False

        i, j = 0, 0
        vDict = defaultdict(int)
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j]!= "." and vDict[board[i][j]] == 1 :
                    return False
                vDict[board[i][j]]+=1
            vDict = defaultdict(int)


        i, j = 0, 0
        sbDict = defaultdict(int)
        while i<len(board):
            while j<len(board[0]):
                for rep_ in range(3):
                    for item in board[i+rep_][j:j + 3]:
                        if item != "." and sbDict[item] == 1:
                            return False
                        sbDict[item] += 1
                j+=3
                sbDict = defaultdict(int)
            i+=3
            j=0


        return True








print(Solution().isValidSudoku([[".",".",".",".","5",".",".","1","."],
                                [".","4",".","3",".",".",".",".","."],
                                [".",".",".",".",".",".",".",".","."],
                                ["8",".",".",".",".",".",".","2","."],
                                [".",".","2",".","7",".",".",".","."],
                                [".","1","5",".",".",".",".",".","."],
                                [".",".",".",".",".","2",".",".","."],
                                [".","2",".","9",".",".",".",".","."],
                                ["2",".","4",".",".",".",".",".","."]]))