def yell(message: str) -> str:
    """
    >>> yell("Can't shake it off of me!")
    "Can't shake it off of me!!"
    >>> yell("Who the hell put the muffins the freezer?")
    'Who the hell put the muffins the freezer??'
    >>> yell("Cringe? CRINGE!")
    'Cringe?? CRINGE!!'
    """
    result = ""
    for letter in message:
        to_add = letter
        if letter in "?!":
            to_add *= 2
        
        result += to_add
    return result
        
if __name__ == "__main__":
    message = input()
    print(yell(message))