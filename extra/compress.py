def compress(lst: list[int]) -> list[list[int, int]]:
    """
    >>> compress([1, 1, 1, 1])
    [[1, 4]]
    >>> compress([1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2])
    [[1, 4], [0, 5], [1, 1], [2, 1]]
    """
    result: list[list[int, int]] = []
    
    i = 0
    while i < len(lst):
        entry = [lst[i], 1]
        
        j = i + 1
        while j < len(lst) and lst[j] == lst[i]:
            entry[1] += 1
            j += 1
        
        i = j
        result.append(entry)
        
    return result
    
def decompress(pairs: list[list[int, int]]) -> list[int]:
    """
    >>> decompress([[1, 4]])
    [1, 1, 1, 1]
    >>> decompress([[1, 4], [0, 5], [1, 1], [2, 1]])
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2]
    """
    result: list[int] = []
    
    for i in range(len(pairs)):
        result += [pairs[i][0]] * pairs[i][1]
        
    return result
    
if __name__ == '__main__':
    NUMBER_EXPERIMENTS = 1000
    total_compression_ratio = 0
    
    for i in range(NUMBER_EXPERIMENTS):
        test_list = [random.randint(0, 9) for _ in range(1000)]
        compressed_list = compress(test_list)
        
        total_compression_ratio += len(test_list) / (2 * len(compressed_list))
    
    print(f"De gemiddelde compressie-ratio voor alle 1000 experimenten: {total_compression_ratio / 1000}")    