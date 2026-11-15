import random
import math

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
SYLLABLE_COUNT = 6

def get_random_group() -> str:
    return random.choice(CONSONANTS) + random.choice(VOWELS) + random.choice(CONSONANTS)

def new_password() -> str:
    """
    Genereert een wachtwoord
    """
    result = ""
    
    for i in range(1, SYLLABLE_COUNT):
        result += get_random_group()
        if i % 2 == 0:
            result += "-"
    
    result += get_random_group()
    
    # Digit placement 
    hyphen_indices = []
    for i in range(len(result)):
        if result[i] == "-":
            hyphen_indices.append(i)
    
    digit_symbol = str(random.randint(0, 9))
    digit_choice = random.randint(0, 4)
    if digit_choice == 0:
        digit_index = hyphen_indices[0] - 1
    elif digit_choice == 1:
        digit_index = hyphen_indices[0] + 1
    elif digit_choice == 2:
        digit_index = hyphen_indices[1] - 1
    elif digit_choice == 3:
        digit_index = hyphen_indices[1] + 1
    else:
        digit_index = len(result) - 1
    
    temp_result = ""
    for i in range(len(result)):
        if digit_index == i:
            temp_result += digit_symbol
        else:
            temp_result += result[i]
    result = temp_result
    # Uppercase letter placement
    uppercase_letter_index = random.randint(0, len(result) - 1)
    while not result[uppercase_letter_index].isalpha():
        uppercase_letter_index = random.randint(0, len(result) - 1)
        
    temp_result = ""
    for i in range(len(result)):
        if uppercase_letter_index == i:
            temp_result += result[i].upper()
        else:
            temp_result += result[i]
    result = temp_result
    
    return result
    
def entropy(string):
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """
    for i in range(10000):
        new_password()

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()