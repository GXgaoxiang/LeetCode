
def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    row3 = ["Z", "X", "C", "V", "B", "N", "M"]
    ls = []
    for w in words:
        result_1 = True
        result_2 = True
        result_3 = True
        upper_words = w.upper()
        for word in upper_words:
            if word not in row1:
                result_1 = False
            if word not in row2:
                result_2 = False
            if word not in row3:
                result_3 = False
        if result_1 or result_2 or result_3:
            ls.append(w)
    return ls
print(findWords(["Alaska"]))
