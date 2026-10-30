def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    >>> count_coins(41)
    4
    >>> count_coins(50)
    2
    >>> count_coins(50)
    2
    """
    count = 0
    
    while cents - 25 >= 0:
        cents -= 25
        count += 1
    
    while cents - 10 >= 0:
        cents -= 10
        count += 1
        
    while cents - 5 >= 0:
        cents -= 5
        count += 1
        
    while cents - 1 >= 0:
        cents -= 1
        count += 1

    return count

if __name__ == '__main__':
    amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
    while amount <= 0:
        amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
    
    print(count_coins(round(amount * 100)))
        