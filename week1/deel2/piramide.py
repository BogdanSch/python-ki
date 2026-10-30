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
        total_spaces = height - (1 + i)
        for j in range()
            print(" ", end="")
        for j in range(i + 2)
            print("#", end="")
        print()

if __name__ == "__main__":
    #  niet groter dan 23
    height = int(input("Hoe hoog moet de piramide zijn? "))
    while height <= 0 or height > 23:
        height = int(input("Hoe hoog moet de piramide zijn? "))
        
    print_piramide(height)