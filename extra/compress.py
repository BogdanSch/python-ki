def compress(lst: list[int]) -> list[tuple[int, int]]:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if