def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -9
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    3
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    9
    """
    words = 0
    letters = 0
    sentences = 0
    is_word = False
    
    for letter in text:
        if letter.isalpha():
            letters += 1
            if not is_word:
                words += 1
                is_word = True
        else:
            if letter in ".;!?":
                sentences += 1
            if letter != "'":
                is_word = False
    return coleman_liau(words, sentences, letters)

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    >>> coleman_liau(10, 1, 20)
    -7
    >>> coleman_liau(30, 5, 50)
    -11
    >>> coleman_liau(30, 1, 60)
    """
    l = 100 * letters / words
    s = 100 * sentences / words
    return round(0.0588 * l - 0.296 * s - 15.8)

if __name__ == '__main__':
    print(coleman_liau(30, 1, 100))
    text = input("Text: ")
    result = calculate_grade(text)
    
    if result < 1:
        print(f"Below Grade 1")
    elif result >= 16:
        print(f"Grade 16+")
    else:
        print(f"Grade {result}")