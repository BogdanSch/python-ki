def longest_word_from_list(lst: list[str]) -> str:
    """
    >>> longest_word_from_list(["kat", "hond", "olifant"])
    'olifant'
    >>> longest_word_from_list(["abc", "defg"])
    'defg'
    """
    longest_word = lst[0]
    
    for i in range(1, len(lst)):
        if len(lst[i]) > len(longest_word):
            longest_word = lst[i]
            
    return longest_word
    
def print_banner(lst: list[str]) -> None:
    """
    >>> lst = ["Margherita", "Tutta", "la", "Vita"]
    >>> print_banner(lst)
    ##########
    Margherita
    Tutta
    la
    Vita
    ##########
    """
    longest_word = longest_word_from_list(lst)
    hash_length = len(longest_word)
    
    print("#" * hash_length)
    for word in lst:
        print(word)
    print("#" * hash_length)
    
def string_to_list(text: str) -> list[str]:
    """
    >>> string_to_list("Hallo wereld")
    ['Hallo', 'wereld']
    >>> string_to_list("Ik leer Python")
    ['Ik', 'leer', 'Python']
    """
    words: list[str] = []
    current_word = ""
    for i in range(len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += text[i]
    if len(current_word) != 0:
            words.append(current_word)
        
            
if __name__ == "__main__":
    message = input("Enter your message: ")
    words = string_to_list(message)
    print_banner(words)