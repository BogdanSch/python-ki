def yell(message: str) -> str:
    result = ""
    for letter in input:
        to_add = letter
        if letter in "?!":
            to_add *= 2
        
        result += to_add
        
if __name__ == "__main__":
    input