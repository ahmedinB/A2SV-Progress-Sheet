from collections import defaultdict
t = int(input())
for t_ in range (t):
    n, m = list(map(int, input().split()))
    chessboard = []
    for n_ in range(n):
        rows = list(map(int, input().split()))
        chessboard.append(rows)

    # Define two dictionaries for diagonal sum
    topLeft_toBottomRight = defaultdict(int)
    topRight_BottomLeft = defaultdict(int)

    # {i : []}
    # {i : int}

    for i in range(n):
        for j in range(m):
            topRight_BottomLeft[i+j] += chessboard[i][j]
            topLeft_toBottomRight[j-i] += chessboard[i][j]
    max_sum = 0
    for i in range(n):
        for j in  range(m):
            sum_ = topRight_BottomLeft[j + i] + topLeft_toBottomRight[j - i] - chessboard[i][j]
            max_sum = max(max_sum, sum_)

    print(max_sum)









    # # create a 2D array to store the diagonal sums
    # diag_sums = [[0] * m for _ in range(n)]
    #
    # # calculate and store the diagonal sums
    # for i in range(n):
    #     for j in range(m):
    #         # check diagonals going to the right-up
    #         for k in range(1, min(n - i, m - j)):
    #             diag_sums[i][j] += chessboard[i + k][j + k]
    #         # check diagonals going to the left-up
    #         for k in range(1, min(n - i, j + 1)):
    #             diag_sums[i][j] += chessboard[i + k][j - k]
    #         # check diagonals going to the right-down
    #         for k in range(1, min(i + 1, m - j)):
    #             diag_sums[i][j] += chessboard[i - k][j + k]
    #         # check diagonals going to the left-down
    #         for k in range(1, min(i + 1, j + 1)):
    #             diag_sums[i][j] += chessboard[i - k][j - k]
    #         diag_sums[i][j] += chessboard[i][j]
    # print(diag_sums)
    # # iterate through the chessboard and find the sum of cells attacked by the bishop
    # for i in range(n):
    #     for j in range(m):
    #         # find the maximum sum of all the diagonal
    #         max_sum = max(max_sum, diag_sums[i][j])
    #
    # print(max_sum)
    #

