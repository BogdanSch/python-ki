def print_piramide(height: int) -> None:
    for i in range(height):
        print(" " * (height - 2) + "#" * (i + 2))

if __name__ == "__main__":
    height = int(input("Hoe hoog moet de piramide zijn? "))
    