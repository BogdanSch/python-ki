def get_positive_int() -> int:
    number = int(input("Enter a positive int: "))
    while number <= 0:
        number = int(input("Enter a positive int: "))

    return number

def get_any_int_but_0() -> int:
    number = int(input("Enter any int except 0: "))
    while number == 0:
        number = int(input("Enter any int except 0: "))

    return number

def get_min_int(minimum: int) -> int:
    number = int(input(f"Enter a number >= {minimum}: "))
    while number < minimum:
        number = int(input("Enter a number >= {minimum}:"))

    return number

def get_two_different_ints() -> tuple:
    

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()