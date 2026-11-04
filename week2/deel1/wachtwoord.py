def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    """
    return len(password) >= 8

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """
    has_uppercase = False
    has_lowercase = False
    
    for letter in password:
        if letter.isupper():
            has_uppercase = True
        elif letter.islower():
            has_lowercase = True
            
        if has_uppercase and has_lowercase:
            return True
    
    return has_uppercase and has_lowercase

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
    """
    return check_length(password) and check_letter(password) and check_number(password)

if __name__ == '__main__':
    password = input("Geef een wachtwoord: ")
    
    if check_password(password):
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")
    