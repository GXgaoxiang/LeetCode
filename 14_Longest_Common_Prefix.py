def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0 or len(strs) ==1:
        return ""
    shortest = min(strs)
    len_shortest = len(shortest)
    while len_shortest >0:
        result = True
        for i in range(len(strs)):
            if strs[i][0:len_shortest] != shortest[:len_shortest]:
                result = False
                break
        if result == True:
            return strs[0][0:len_shortest]
        len_shortest -= 1
    return ""


print(longestCommonPrefix(["flower","flow","flight"]))