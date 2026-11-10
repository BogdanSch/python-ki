def uniq(lst: list[object]) -> list[object]:
    """
    >>> uniq([1, 1, 1, 2, 3, 4, 0, -1, 0])
    [1, 2, 3, 4, 0, -1]
    >>> uniq([1, 1, 1, 2, 3, 4, 0, -1, 0])
    """
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst