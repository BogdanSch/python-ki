def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """
    first = lst[0]
    for i in range(len(lst)):
        rotated_lst.append(lst[i])
    rotated_lst.append(first)
