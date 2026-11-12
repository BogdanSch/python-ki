POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.
    """

def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.
    """
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    if letter not in ALPHABET:
        return 0
    
    

if __name__ == '__main__':
    player1_word = input("Speler 1: ")
    player2_word = input("Speler 2: ")