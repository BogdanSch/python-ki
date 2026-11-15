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
    
    for i in range(1, 7):
        result += get_random_group()
        if i % 2 == 0:
            result += "-"
    
    # Digit placement 
    hyphen_indices = []
    for i in range(len(result)):
        if result[i] == "-":
            hyphen_indices.append(i)
    
    digit = random.randint(9)
    digit_choice = random.randint(4)
    if digit_choice == 0:
        result[]
    # Uppercase letter placement
    

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()