# 我的方法， 所用时间长，花了176ms
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = {}
        for candy in candies:
            if candy not in dic:
                dic[candy] = 1
        len_candy = len(dic.keys())
        amount = len(candies) // 2
        if amount > len_candy:
            return len_candy
        else:
            return amount
# 网上的方法， 只用了92ms,超过了98%
# 注意一下python里面的set用法，很方便的一个东西
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)/2,len(set(candies)))