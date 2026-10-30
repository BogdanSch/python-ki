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
        print(" " * (height - (1 + i)) + "#" * (i + 2))

if __name__ == "__main__":
    #  niet groter dan 23
    height = int(input("Hoe hoog moet de piramide zijn? "))
    while <= 0 or 
    print_piramide(height)