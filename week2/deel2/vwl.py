def remove_vowels(s: str) -> str:
    """
    >>> verberg_klinkers("Python")
    'pythn'
    >>> verberg_klinkers("Amsterdam")
    '*mst*rd*m'
    """
    new_string = ""
    for char in s:
        if not in "aeiouAEIOU":
            new_string += char
    return new_string
    
if __name__ == "__main__":
    text = input("")
    print(remove_vowels(text))