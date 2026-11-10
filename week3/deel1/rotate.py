def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """
    rotated_lst = []
    for i in range(len(lst) - 1):
        rotated_lst.append(lst[i])

if __name__ == "__main__":

    