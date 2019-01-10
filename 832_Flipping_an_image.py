class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ls = []
        for sub in A:
            sub = sub[::-1]
            sub = [(s+1)%2 for s in sub ]
            ls.append(sub)
        return ls