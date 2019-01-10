def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < -(1 << 31) or x > (1 << 31) - 1:
        print(1)
        return 0
    num = str(x)
    if num[0] == "-":
        num = num[1:]
        re_num = "-" + num[::-1]
    else:
        re_num = num[::-1]
    if int(re_num) < -(1 << 31) or int(re_num) > (1 << 31 )- 1:
        print(2)
        return 0
    return int(re_num)

print(reverse(1463847412))