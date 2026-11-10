def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 2)
    [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]
    >>> chunk([], 3)
    []
    """
    new_lst = []
    sub_lst = []
    for i in range(len(lst)):
        if len(sub_lst) == n:
            new_lst.append(sub_lst)
        else:
            sub_lst.append
            
    return new_lst
    