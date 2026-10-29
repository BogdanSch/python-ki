def is_schrikkel(y: int) -> bool:
    """
    Bepaalt of een jaar schrikkeljaar is.
    
    >>> is_schrikkel(2024)
    True
    >>> is_schrikkel(2023)
    False
    >>> is_schrikkel(1900)
    False
    >>> is_schrikkel(2000)
    True
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

if __name__ == "__main__":
    year = int(input())
    if is_schrikkel(year):
        print(f"{year} is een schrikkeljaar")
    else:
        print(f"{year} is geen schrikkeljaar")
        