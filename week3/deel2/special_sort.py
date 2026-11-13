def special_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    >>> special_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    >>> special_sort([])
    []
    >>> selection_sort([0])
    [0]
    >>> selection_sort([1, 0, 2, -99, 3, 5])
    [-99, 0, 1, 2, 3, 5]
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l
            