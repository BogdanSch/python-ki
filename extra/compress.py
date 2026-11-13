def compress(lst: list[int]) -> list[list[int, int]]:
    result = []
    for i in range(len(lst)):
        entry = [lst[i]]
        
        int j = i + 1
        while lst[j] == lst[i]:
            entry.