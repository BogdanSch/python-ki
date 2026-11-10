def compact(lst: list[object]) -> list[object]:
    """
    >>> compact([1, '', True, 'abcd', 5])
    [1, True, 'abcd', 5]
    >>> compact([1, '', True, 'abcd', 5])
    """
    return [item for item in lst if item != False and item !=  0 and item != '']