def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    for i in range(len(l)):
        min_element_index: int = i
        for j in range(i, len(l)):
            if l[j] < l[min_element_index]:
                min_element_index = j
        
        if min_element_index != i:
        l[i] = min_element
    
    return l