def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    start,end,max_len = 0,0,0
    map = {}
    while start < len(s) and end < len(s):
        if s[end] in map.keys():
            # 这里的man(start.....)保证了start不会往回倒退
            start = max(start, map[s[end]] + 1)
        map[s[end]] = end
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len

