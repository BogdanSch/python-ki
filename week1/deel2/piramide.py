def print_piramide(height: int) -> None:
    for i in range(height):
        print(" " * (i) + "#" * i)        
    ##
   ###
  ####
 #####
######

if __name__ == "__main__":
    height = int(input("Hoe hoog moet de piramide zijn? "))
    