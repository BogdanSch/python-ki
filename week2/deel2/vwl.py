def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels("Python")
    'Pythn'
    >>> remove_vowels("Amsterdam")
    'mstrdm'
    """
    new_string = ""
    for char in s:
        if char not in "aeiouAEIOU":
            new_string += char
    return new_string
    
if __name__ == "__main__":
    text = input("")
    print(remove_vowels(text))