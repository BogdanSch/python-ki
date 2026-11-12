def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig([5, 6, 7, 8])
    [[5, 6, 7, 8]]
    >>> contig([1, 3, 5])
    [[1], [3], [5]]
    >>> contig([])
    []
    >>> contig([1])
    [[1]]
    """
    if len(lst) < 1:
        return []
        
    new_list: list[list[int]] = []
    sub_list: list[int] = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] - 1 == lst[i - 1]:
            sub_list.append(lst[i])
        else:
            new_list.append(sub_list)
            sub_list = [lst[i]]
    if len(sub_list) != 0:
        new_list.append(sub_list)
        
    return new_list