import random

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
PASSWORD_LENGTH = 20

def new_password() -> str:
    """
    Genereert een wachtwoord
    """
    result = random.choice(CONSONANTS)
    
    for i in range(1, 20):
        if i % 2 == 0:
            result += random.choice(CONSONANTS)
        else:
            result += random.choice(VOWELS)
    
    

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()