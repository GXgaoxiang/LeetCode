def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    ls = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
          "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
          "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
    amount = []
    for word in words:
        code = ""
        for letter in word:
            code = code+ls[letter]
        if code not in amount:
            amount.append(code)
    return amount
print(uniqueMorseRepresentations(["vtpke","vngc","vnqr","gbzx","qvdx"]))