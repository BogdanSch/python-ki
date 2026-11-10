def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2)
    [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]
    >>> chunk([], 3)
    []
    """
    new_lst = []
    for i in range(0, len(lst), n):
        sub_lst = []
        for j in range(i, i + n):
            sub_lst.append()
            
        new_lst.append(lst[i:(i + n)])
    return new_lst
    