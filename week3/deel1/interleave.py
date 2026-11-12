def interleave(lst1: list[object], lst2: list[object], keep: bool) -> list[object]:
    """
    >>> interleave([], [], True)
    []
    >>> interleave([1, 3, 5], [2, 4, 6], False)
    [1, 2, 3, 4, 5, 6]
    >>> interleave([1, 3, 5, 7], [2, 4, 6, 8, 9, 10], False)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # if len(lst1) == 0 and len(lst2) == 0:
    #     return []
        
    new_list = []
    min_length = min(len(lst1), len(lst2))
    
    for i in range(min_length):
        new_list.append(lst1[i])
        new_list.append(lst2[i])
    
    if keep and len(lst1) > min_length:
        for i in range(min_length, len(lst1)):
            new_list.append(lst1[i])
    elif keep and len(lst2) > min_length:
        for i in range(min_length, len(lst2)):
            new_list.append(lst2[i])
    
    return new_list