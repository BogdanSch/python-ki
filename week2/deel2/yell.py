def yell(message: str) -> str:
    """
    >>> yell()
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