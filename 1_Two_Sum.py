def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i
    for j in range(len(nums)):
        value = target - nums[j]
        if value in dic.keys():
            if dic[value] != j:
                ls = [j, dic[value]]
                return ls