def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    >>> selection_sort([])
    []
    >>> selection_sort([0])
    [0]
    >>> selection_sort([1, 0, 2, -99, 3])
    [0]
    """
    for i in range(len(l)):
        min_element_index: int = i
        for j in range(i, len(l)):
            if l[j] < l[min_element_index]:
                min_element_index = j
        
        if min_element_index != i:
            l[i], l[min_element] = l[min_element], l[i]
    
    return l