
# 想法就是第一个出现I的地方就赋值0，第一个出现D的地方就赋值len(S),然后之后每碰到就进行自增或者自减（贪心思想）
# 最后一个在for外面的append，用max_num或者min_num都可以，因为此时这两个的值是一样的
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        max_num = len(S)
        min_num = 0
        permutation = []
        for s in S:
            if s == "I":
                permutation.append(min_num)
                min_num += 1
            if s == "D":
                permutation.append(max_num)
                max_num -=1
        permutation.append(min_num)
        return permutation