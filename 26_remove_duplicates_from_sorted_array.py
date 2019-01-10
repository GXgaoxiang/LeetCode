# 自己做的：
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i = i + 1
    return len(nums)

# 网上找的比较快的
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    j = 1
    size = len(nums)
    while j < size:
        if nums[j] == nums[i - 1]:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    return min(i, size)