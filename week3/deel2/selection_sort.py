def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    for i in range(len(l)):
        min_element: int = l[i]
        for j in range(i, len(l)):
            if l[j] < min_element:
                min_element
    
    return l