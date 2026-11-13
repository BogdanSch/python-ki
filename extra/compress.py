def compress(lst: list[int]) -> list[list[int, int]]:
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                result.