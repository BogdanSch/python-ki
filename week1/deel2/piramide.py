def print_piramide(height: int) -> None:
    """
    >>> print_piramide(5)
        ##
       ###
      ####
     #####
    ######
    """
    for i in range(height):
        print(" " * (height - (1 + i)) + "#" * (i + 2))

if __name__ == "__main__":
    height = int(input("Hoe hoog moet de piramide zijn? "))
    print_piramide(height)