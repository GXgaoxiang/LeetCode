# 注意找到的规律
# 出现1则加4，如果此点的左上以及左边同时也是1，那么就重复了两条边，则减2
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 4
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        count -= 2
                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        count -= 2
        return count
