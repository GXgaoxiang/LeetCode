# 自己的方法比较繁琐，下面是两个比较方便的方法，其中方法2 faster than 99.57%
# 题目没什么特别的，这里主要是列表生成式需要多学习一下
# 方法1
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res

# 方法2
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]