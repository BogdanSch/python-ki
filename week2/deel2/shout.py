def shout(text: str) -> str:
    """
    >>> shout('Who the hell put the muffins the freezer?')
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'
    >>> shout('Cringe!')
    'CRINGE!'
    >>> shout('')
    
    """
    new_text = ""
    for char in text:
        new_text += char.upper()
    return new_text

if __name__ == "__main__":
    # 
    text = input()
    print(shout(text))
    