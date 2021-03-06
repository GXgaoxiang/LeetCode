def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    while left<=right:
        middle = (left+right)//2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle+1
        if nums[middle] > target:
            right = middle-1
    return right +1


