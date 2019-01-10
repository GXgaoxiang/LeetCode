def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def func(nums):
        len_nums = len(nums)
        if len_nums < 2:
            ls2 = []
            ls2.append(nums)
            return ls2
        else:
            ls = []

            for i in range(len_nums):
                ch = nums[i]
                rest = nums[0:i] + nums[i + 1:len_nums]

                for sub in func(rest):
                    l = []
                    l.append(ch)
                    for k in sub:
                        l.append(k)
                    ls.append(l)
        return ls

    return func(nums)