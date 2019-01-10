class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_num = max(A)
        min_num = min(A)
        if max_num - K <= min_num + K:
            return 0
        else:
            result = max_num - min_num - 2 * K
            return result
