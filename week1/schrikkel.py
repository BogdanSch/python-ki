def is_leap_year(y: int) -> bool:
    """
    Bepaalt of een jaar 
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

if __name__ == "__main__":
    year = int(input())
    if is_leap_year(year):
        print(f"{year} is een schrikkeljaar")
    else:
        print(f"{year} is geen schrikkeljaar")
        