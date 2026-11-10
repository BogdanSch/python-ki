def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    """
    new_lst = []
    for i in range(0, len(lst), n):
        new_lst.append(lst[i:(i + n + 1)])
    return new_lst
    