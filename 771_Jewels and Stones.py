# 我的方法
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jewels = list(J)
        count = 0
        for i in S:
            if i in Jewels:
                count = count +1
        return count
# 更简便的方法，但是时间没有优化
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)