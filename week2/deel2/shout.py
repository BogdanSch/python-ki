def shout(text: str) -> str:
    """
    >>> shout('Who the hell put the muffins the freezer?')
    
    """
    new_text = ""
    for char in text:
        new_text += char.upper()

if __name__ == "__main__":
    # 
    text = input()
    