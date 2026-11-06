def remove_vowels(s: str) -> str:
    """
    >>> verberg_klinkers("Python")
    'Pythn'
    >>> verberg_klinkers("Amsterdam")
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