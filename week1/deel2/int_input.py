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
    number = int(input(f"Enter an int >= {minimum}: "))
    while number < minimum:
        number = int(input(f"Enter an int >= {minimum}:"))

    return number

def get_two_different_ints() -> tuple:
    number1 = int(input(f"Enter the first unique int: "))
    number2 = int(input(f"Enter the second unique int: "))
    while number1 == number2:
        number2 = int(input("Enter a unique int: "))

    return number1, number2

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()