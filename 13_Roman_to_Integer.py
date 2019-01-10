def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    digital_num = 0
    for i in range(len(s) - 1):
        if (dic[s[i]] < dic[s[i + 1]]):
            digital_num -= dic[s[i]]
        else:
            digital_num += dic[s[i]]
    digital_num += dic[s[-1]]
    return digital_num