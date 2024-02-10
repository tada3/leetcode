

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        return grid[-1][-1]
    
def main(grid):
    print(f'Input: grid = {grid}')
    ret = Solution().minPathSum(grid)
    print(f'Output: {ret}')


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]


    main(grid)