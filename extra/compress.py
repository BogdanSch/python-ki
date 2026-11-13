def compress(lst: list[int]) -> list[list[int, int]]:
    """
    >>> compress([1, 1, 1, 1])
    [[1, 4]]
    """
    result = []
    
    while i < len(lst):
        entry = [lst[i], 1]
        
        j = i + 1
        while lst[j] == lst[i]:
            entry[1] += 1
            j += 1
        
        i = j
        result.append(entry)
        
    return result