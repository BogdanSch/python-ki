def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig()
    """
    new_list: list[list[int]] = [[lst[0]]]
    for i in range(len(lst)):
        