class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        right = len(A)-1
        left = 0
        while left< right:
            mid = (left+right)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]<A[mid-1] and A[mid]>A[mid+1]:
                right = mid
            else:
                left = mid