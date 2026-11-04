def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    
    """
    words = 0
    letters = 0
    sentences = 0
    for letter in text:
        if 

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """
    l = 100 * letters / words
    s = 100 * sentences / words
    return round(0.0588 * l - 0.296 * s - 15.8)

if __name__ == '__main__':
    text = input("Text: ")
    print(f"Grade {calculate_grade(text)}")