def longest_word_from_list(lst: list[string]) -> str:
    longest_word = lst[0]
    
    for i in range(1, len(lst)):
        if len(lst[i]) > len(longest_word):
            longest_word = lst[i]
    return longest_word