# 我的方法：
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_A = A.split(" ")
        words_B = B.split(" ")
        dic = {}
        ls = []
        for word in words_A:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
        for word in words_B:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
        for key, value in dic.items():
            if value == 1:
                ls.append(key)
        return ls
# 网上方法
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        C = (A + ' ' + B).split(' ')
        ans = []
        for word in C:
            if C.count(word) == 1:
                ans.append(word)
        return ans

