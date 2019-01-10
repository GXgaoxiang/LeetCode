class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ls = []
        for i in range(left,right+1):
            original = i
            result = True
            while i >0:
                num=i%10
                if num == 0:
                    result = False
                    break
                i = i//10
                if original % num !=0:
                    result = False
                    break
            if result == True:
                ls.append(original)
        return ls