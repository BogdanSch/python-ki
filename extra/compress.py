def compress(lst: list[int]) -> list[tuple[int, int]]:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                