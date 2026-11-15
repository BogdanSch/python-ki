import random

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
PASSWORD_LENGTH = 20

def get_random_group() -> str:
    return random.choice(CONSONANTS) + random.choice(VOWELS) + random.choice(CONSONANTS)

def new_password() -> str:
    """
    Genereert een wachtwoord
    """
    result = ""
    first_hyphen_in
    
    for i in range(1, 7):
        result += get_random_group()
        if i % 2 == 0:
            result += "-"
    
    # Digit placement 
    
    # Uppercase letter placement
    

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()