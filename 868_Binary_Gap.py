class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_N = bin(N)[2:]
        ls = []
        index_before = 0
        for index, n in enumerate(bin_N):
            if n == "1":
                ls.append(index - index_before)
                index_before = index

        return max(ls)
