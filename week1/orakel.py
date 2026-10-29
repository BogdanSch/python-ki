def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties 
    42, tweeenveertig, of tweeënveertig is.
    return: bool
    
    >>>check_answer("42")
    True
    >>>check_answer("tweeenveertig")
    True
    >>>check_answer("tweeënzestig")
    False
        >>>check_answer("tweeenveertig")
    True
    """
    return answer == "42" or answer == "tweeenveertig" or answer == "tweeënveertig"

if __name__ == '__main__':
    <Vraag hier de gebruiker om een antwoord, roep je functie aan, en print het oordeel>