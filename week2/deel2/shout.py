def shout(text: str) -> str:
    new_text = ""
    for char in text:
        new_text += char.upper()

if __name__ == "__main__":
    # Who the hell put the muffins the freezer?
    text = input()
    