def longest_word_from_list(lst: list[string]) -> str:
    """
    >>> longest_word_from_list()
    
    >>> longest_word_from_list([])
    
    """
    longest_word = lst[0]
    
    for i in range(1, len(lst)):
        if len(lst[i]) > len(longest_word):
            longest_word = lst[i]
            
    return longest_word
    
def print_banner(lst: list[string]) -> None:
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
    words: list[str] = []
    current_word = ""
    for i in range(len(text)):
        if text[i] == " ":
            words.append(current_word)
        else:
            current_word += text[i]