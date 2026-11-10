def compact(lst: list[object]) -> list[object]:
    """
    >>> compact([1, '', True, 'abcd', 5])
    [1, True, 'abcd', 5]
    >>> compact([False, ''])
    []
    >>> compact([])
    []
    """
    new_lst = []
    for item in lst: 
        if item:
            new_lst.append(item)
    return new_lst