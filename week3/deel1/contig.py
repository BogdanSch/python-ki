def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig()
    """
    new_list: list[list[int]] = []
    sub_list: list[int] = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] - 1 == lst[i - 1]:
            sub_list.append(lst[i])
        new_list.append(sub_list)
        