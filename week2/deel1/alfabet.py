def compare(word1: str, word2: str) -> int:
    """
    >>> compare("Taylor", "Lana")
    1
    >>> compare("shark", "sWoRd")
    -1
    >>> compare("Daantje", "Daan")
    1
    >>> compare("amanda", "Amanda")
    0
    """
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        lower_letter_word1 = word1[i].lower()
        lower_letter_word2 = word2[i].lower()
        
        if lower_letter_word1 < lower_letter_word2:
            return -1
        elif lower_letter_word1 > lower_letter_word2:
            return 1
    
    if len(word1) > len(word2):
        return 1
    elif len(word1) < len(word2):
        return -1
    return 0

if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    
    result = compare(word1, word2)
    if result == 0:
        print("No need to decide!")
    elif result == -1:
        print(word1 + " first")
    else:
        print(word2 + " first")
        