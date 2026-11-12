def interleave(lst1: list[object], lst2: list[object], keep: bool) -> list[object]:
    """
    >>> interleave([], [], True)
    []
    >>>
    """
    new_list = []
    min_length = min(len(lst1), lst2)
    
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