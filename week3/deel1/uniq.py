def uniq(lst: list[object]) -> list[object]:
    """
    
    """
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst