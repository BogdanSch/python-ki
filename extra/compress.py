def compress(lst: list[int]) -> list[list[int, int]]:
    result = []
    
    while i < len(lst):
        entry = [lst[i], 1]
        
        int j = i + 1
        while lst[j] == lst[i]:
            entry[1] += 1
        
        result.append(entry)
        i = j