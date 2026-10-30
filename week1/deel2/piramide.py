def print_piramide(height: int) -> None:
    """
    >>> print_piramide(5)
        ##
       ###
      ####
     #####
    ######
    >>> print_piramide(3)
      ##
     ###
    ####
    """
    for i in range(height):
        for j in range(height - (1 + i) + 1)
            print(" " * () )
        for j in range((i + 2))

if __name__ == "__main__":
    #  niet groter dan 23
    height = int(input("Hoe hoog moet de piramide zijn? "))
    while height <= 0 or height > 23:
        height = int(input("Hoe hoog moet de piramide zijn? "))
        
    print_piramide(height)