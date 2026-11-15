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
    
    for i in range(1, PASSWORD_LENGTH // 3 + 1):
        result += get_random_group()
        if i % 2 == 0:
            result += "-"
    
    # Digit placement 
    hyphen_indices = []
    for i in range(len(result)):
        if result[i] == "-":
            hyphen_indices.append(i)
    
    digit_index
    digit_symbol = str(random.randint(0, 9))
    digit_choice = random.randint(0, 4)
    if digit_choice == 0:
        result[hyphen_indices[0] - 1] = digit_symbol
    elif digit_choice == 1:
        result[hyphen_indices[0] + 1] = digit_symbol
    elif digit_choice == 2:
        result[hyphen_indices[1] - 1] = digit_symbol
    elif digit_choice == 3:
        result[hyphen_indices[1] + 1] = digit_symbol
    else:
        result = result[:-2] + digit_symbol
    # Uppercase letter placement
    uppercase_letter_index = random.randint(0, len(result))
    while not result[uppercase_letter_index].isalpha():
        uppercase_letter_index = random.randint(0, len(result))
    result = result[0:uppercase_letter_index] + result[uppercase_letter_index].upper() + result[uppercase_letter_index:-1]
    
    return result

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()