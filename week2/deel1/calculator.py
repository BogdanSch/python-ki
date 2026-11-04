def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    >>> evaluate(1, '+', 1)
    2.0
    >>> evaluate(100, '-', 9)
    91.0
    >>> evaluate(1, '+', 1)
    2.0
    """
    result = float(x)
    if y == "+":
        result += z
    elif y == "-":
        result -= z
    elif y == "*":
        result *= z
    elif y == "/":
        result /= z

if __name__ == '__main__':
    elements = input("").split(" ")
    x = int(elements[0])
    y = elements[1]
    z = int(elements[2])
    
    print(evaluate(x, y, z)