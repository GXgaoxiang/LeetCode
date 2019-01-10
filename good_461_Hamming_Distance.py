
# 这道题是从网上查来的。
# bin是python自带的一个转换为二进制的函数
# ^是异或操作，相同的为0，不同则为1

# 方法①
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")








# 方法②
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while (x!=0 or y!=0):
            if x&0x1 != y&0x1:
                count = count+1
            x = x>>1
            y = y>>1
        return count
"""
 & 按位与------同时为1则为1，否则为0
    应用: ①：清零，如果想将一个单元清零，就可以直接将这个单元&0
          ②：取一个数中指定位，例如取X的最低4个位  就用00001111取
 | 按位或-------有一个为1则为1，否则为0
    应用：①：将某一个数值的某个位置置为1
 负数按补码的形式参与运算
"""
