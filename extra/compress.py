def compress(lst: list[int]) -> list[list[int, int]]:
    result = []
    for i in range(len(lst)):
        entry = [lst[i]]
        
        int j = i + 1
        while lst[j] != lst[i]:
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                result.