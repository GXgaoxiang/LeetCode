class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ls1 = [x for x in A if x%2==0]
        ls2 = [y for y in A if y%2==1]
        return ls1 +ls2