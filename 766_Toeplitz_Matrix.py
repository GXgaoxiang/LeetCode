# 这道题不是很难，就只用判断每一个点和他右下角的那个点进行比较就可以了

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows - 1):
            for col in range(cols - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        return True

