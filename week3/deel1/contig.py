def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig([5, 6, 7, 8])
    [[5, 6, 7, 8]]
    >>> contig([1, 3, 5])
    """
    new_list: list[list[int]] = []
    sub_list: list[int] = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] - 1 == lst[i - 1]:
            sub_list.append(lst[i])
        else:
            new_list.append(sub_list)
            sub_list = [lst[i]]
            
    return new_list