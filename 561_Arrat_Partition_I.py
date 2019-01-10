class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums,reverse=False)
        result = 0
        for i in range(len(nums)//2):
            result +=sorted_nums[2*i]
        return result