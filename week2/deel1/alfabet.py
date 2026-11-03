def compare(word1: str, word2: str) -> int:
    """
    >>>
    """
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        lower_letter_word1 = word1[i].lower()
        lower_letter_word2 = word2[i].lower()
        
        if lower_letter_word1 < lower_letter_word2:
            return -1
        elif lower_letter_word1 > lower_letter_word2:
            return 1
    
    
    for i in range(min_length, ):
        

    return 0
            
    
    
    

if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    
    if compare(word1, word2) == 0:
        print("No need to decide!")
    elif 