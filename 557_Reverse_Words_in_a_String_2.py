
# 我的方法 用了84ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result = ""
        for index, word in enumerate(words):
            word = word[::-1]
            if index != len(words) - 1:
                result += word + " "
            else:
                result += word
        return result

# 网上的方法， 用了44ms, 要注意python中join的用法
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        ls = []
        for word in words:
            word = word[::-1]
            ls.append(word)
        return " ".join(ls)

