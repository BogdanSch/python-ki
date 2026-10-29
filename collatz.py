def print_collatz(n: int) -> None:
    current = n
    while current != 1:
        print(current)
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
    print(1)

def collatz_length(n: int) -> int:
    """
    Geeft de lengte van de Collatz-reeks vanaf n.

    >>> collatz_length(1)
    1

    >>> collatz_length(2)
    2

    >>> collatz_length(3)
    8
    """
    count: int = 0
    
    current = n
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
        count += 1
        
    return count

if __name__ == "__main__":
    n = int(input())
    
    