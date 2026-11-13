def compress(lst: list[int]) -> list[list[int, int]]:
    """
    >>> compress([1, 1, 1, 1])
    [[1, 4]]
    >>> compress([1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2])
    [[1, 4], [0, 5], [1, 1], [2, 1]]
    """
    result = []
    
    i = 0
    while i < len(lst):
        entry = [lst[i], 1]
        
        j = i + 1
        while j < len(lst) and lst[j] == lst[i]:
            entry[1] += 1
            j += 1
        
        i = j
        result.append(entry)
        
    return result
    
def decompress(list[list[int, int]])