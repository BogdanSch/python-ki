def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties 
    42, tweeenveertig, of tweeënveertig is.
    
    >>> check_answer("42")
    True
    >>> check_answer("tweeenveertig")
    True
    >>> check_answer("tweeënzestig")
    False
    >>> check_answer("tweeënveertig")
    True
    """
    return answer == "42" or answer == "tweeenveertig" or answer == "tweeënveertig"

if __name__ == '__main__':
    x = input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?")
    
    if check_answer(x):
        print("Ja")
    else:
        print("Nee")