def findComplement( num):
    """
    :type num: int
    :rtype: int
    """
    result = 0
    count = 0
    bin_num = bin(num)[2:]
    string_num = str(bin_num)
    new_num = []
    print(string_num)
    for index,s in enumerate(string_num):
        if s == "1":
            new_num.append(0)
        if s == "0":
            new_num.append(1)
    print(new_num)
    for s in range(len(new_num)-1,-1,-1):
        result += pow(2, count) * new_num[s]
        count += 1
    return result
print(findComplement(2))