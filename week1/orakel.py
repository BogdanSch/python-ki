def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties 
    42, tweeenveertig, of tweeënveertig is.
    
    >>>check_answer("42")
    
    """
    return answer == "42" or answer == "tweeenveertig" or answer == "tweeënveertig"

if __name__ == '__main__':
    <Vraag hier de gebruiker om een antwoord, roep je functie aan, en print het oordeel>