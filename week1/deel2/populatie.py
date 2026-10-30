def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    
    >>> calculate_years(1200, 1300)
    1
    >>> calculate_years(9, 18)
    1
    >>> calculate_years(20, 1300)
    1
    """
    current_size = start_size
    years_total = 0
    
    while current_size < end_size:
        total_birth = current_size // 3
        total_death = current_size // 4
        
        current_size += total_birth - total_death
        years_total += 1
    
    return years_total

if __name__ == '__main__':
    start_size = int(input("Startgrootte: "))
    while start_size < 9:
        start_size = int(input("Startgrootte: "))
    
    end_size = int(input("Eindgrootte: "))
    while end_size <= start_size:
        end_size = int(input("Eindgrootte: "))
        
    print(f"Jaren {calculate_years(start_size, end_size)}")
        