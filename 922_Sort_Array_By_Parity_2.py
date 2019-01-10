
# 我的方法 要跑188ms
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index_odd = 1
        index_even = 0
        new_A = A.copy()
        for a in A:
            if a % 2 == 0:
                new_A[index_even] = a
                index_even += 2
            else:
                new_A[index_odd] = a
                index_odd += 2
        return new_A

# 网上的方法， 和我的时间差不多
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x : x % 2)
        N = len(A)
        res = []
        for i in range(N // 2):
            res.append(A[i])
            res.append(A[N - 1 - i])
        return res


