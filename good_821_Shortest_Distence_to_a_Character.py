
# 用了两遍计算，从左到右，和从右到左，最后取最小值

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        length = len(S)
        max_index = 100000
        ls = [0] * length

        for index, s in enumerate(S):
            if s == C:
                max_index = index
            ls[index] = abs(index - max_index)

        max_index = 10000
        for index in range(len(S) - 1, -1, -1):
            if S[index] == C:
                max_index = index
            ls[index] = min(ls[index], max_index - index)
        return ls


