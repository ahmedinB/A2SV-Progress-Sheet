class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i, j = 0, 2
        row = len(grid)
        col = len(grid[0])
        maxsum = float('-inf')
        while i < row-2:
            sum = grid[i][0] + grid[i][1] + grid[i][2] + grid[i+1][1] + \
              grid[i+2][0] + grid[i+2][1] + grid[i+2][2]
            maxsum = max(maxsum,sum)
            while j < col-1:
                sum = sum + grid[i][j+1] + grid[i+1][j] + grid[i+2][j+1] \
                      - grid[i][j-2] - grid[i+1][j-1] - grid[i+2][j-2]
                maxsum = max(maxsum,sum)
                j+=1
            j=2
            i+=1
        return maxsum

S = Solution()
print(S.maxSum([[520626,685427,788912,800638,717251,683428],[23602,608915,697585,957500,154778,209236],[287585,588801,818234,73530,939116,252369]]))
print(S.maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,11,2,9]]))
print(S.maxSum([[644460,685523,769890,443393,285711],
                [9006,254379,969969,601034,689057],
                [440814,157646,571484,325351,493670],
                [569808,429678,388256,869440,914745],
                [589854,183767,503184,511695,980066],
                [33725,397553,968569,423475,75219]]))
