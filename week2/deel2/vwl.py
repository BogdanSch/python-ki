def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels()
    """
    new_string = ""
    for char in s:
        if not in "aeiouAEIOU":
            new_string += char
    return new_string
    
if __name__ == "__main__":
    text = input("")
    print(remove_vowels()