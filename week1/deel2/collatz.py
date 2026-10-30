def print_collatz(n: int) -> None:
    """
    Print de Collatz-reeks vanaf n.

    >>> print_collatz(1)
    1
    >>> print_collatz(3)
    3
    10
    5
    16
    8
    4
    2
    1
    """
    
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
    count: int = 1
    
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
    print_collatz(n)
    